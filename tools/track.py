#!/usr/bin/env python3
"""track — a CLI-first accomplishment tracker for Computer-assisted work.

Logs completed tasks into ~/.mirrornode/accomplishments.json and generates
weekly markdown summaries, CSV exports, and statistics. Pure stdlib.
"""

import argparse
import csv
import datetime as dt
import io
import json
import os
import re
import subprocess
import sys
import uuid
from collections import Counter
from pathlib import Path

# --------------------------------------------------------------------------- #
# Paths
# --------------------------------------------------------------------------- #

HOME_DIR = Path.home() / ".mirrornode"
DATA_FILE = HOME_DIR / "accomplishments.json"
SUMMARY_DIR = HOME_DIR / "summaries"

SOURCE_DEFAULT = "computer"


# --------------------------------------------------------------------------- #
# Color
# --------------------------------------------------------------------------- #

class C:
    """ANSI color codes, disabled when NO_COLOR is set or output is not a tty."""

    _enabled = True

    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"

    @classmethod
    def init(cls):
        if os.environ.get("NO_COLOR") is not None or not sys.stdout.isatty():
            cls._enabled = False

    @classmethod
    def wrap(cls, code, text):
        if not cls._enabled:
            return text
        return f"{code}{text}{cls.RESET}"


def c_bold(t): return C.wrap(C.BOLD, t)
def c_dim(t): return C.wrap(C.DIM, t)
def c_red(t): return C.wrap(C.RED, t)
def c_green(t): return C.wrap(C.GREEN, t)
def c_yellow(t): return C.wrap(C.YELLOW, t)
def c_blue(t): return C.wrap(C.BLUE, t)
def c_cyan(t): return C.wrap(C.CYAN, t)


# --------------------------------------------------------------------------- #
# Git helpers
# --------------------------------------------------------------------------- #

def _git(args):
    """Run a git command, returning stripped stdout or None on failure."""
    try:
        out = subprocess.run(
            ["git"] + args,
            capture_output=True,
            text=True,
            check=True,
        )
        return out.stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None


def in_git_repo():
    return _git(["rev-parse", "--is-inside-work-tree"]) == "true"


def git_head():
    return _git(["log", "-1", "--format=%H"])


def git_remote_url():
    return _git(["remote", "get-url", "origin"])


def parse_repo_name(remote_url):
    """Extract 'org/repo' from an SSH or HTTPS git remote URL."""
    if not remote_url:
        return None
    url = remote_url.strip()
    if url.endswith(".git"):
        url = url[:-4]
    # SSH form: git@host:org/repo
    m = re.match(r"^[^@]+@[^:]+:(.+)$", url)
    if m:
        return m.group(1)
    # HTTPS/other form: scheme://host/org/repo
    m = re.match(r"^[a-zA-Z]+://[^/]+/(.+)$", url)
    if m:
        return m.group(1)
    return None


def github_base_url(remote_url):
    """Return 'https://github.com/org/repo' from a remote URL, or None."""
    if not remote_url:
        return None
    url = remote_url.strip()
    if url.endswith(".git"):
        url = url[:-4]
    # SSH form: git@host:org/repo
    m = re.match(r"^[^@]+@([^:]+):(.+)$", url)
    if m:
        host, path = m.group(1), m.group(2)
        return f"https://{host}/{path}"
    # Scheme form: scheme://[userinfo@]host/org/repo
    m = re.match(r"^[a-zA-Z]+://(?:[^/@]+@)?([^/]+)/(.+)$", url)
    if m:
        host, path = m.group(1), m.group(2)
        return f"https://{host}/{path}"
    return None


def build_commit_url(remote_url, commit_hash):
    base = github_base_url(remote_url)
    if base and commit_hash:
        return f"{base}/commit/{commit_hash}"
    return None


# --------------------------------------------------------------------------- #
# Storage
# --------------------------------------------------------------------------- #

def ensure_dirs():
    HOME_DIR.mkdir(parents=True, exist_ok=True)
    SUMMARY_DIR.mkdir(parents=True, exist_ok=True)


def load_entries():
    if not DATA_FILE.exists():
        return []
    try:
        with DATA_FILE.open("r", encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError as exc:
        raise SystemExit(
            c_red(f"Refusing to overwrite invalid audit file: {DATA_FILE}")
            + "\nFix or remove it manually."
        ) from exc
    except OSError as exc:
        raise SystemExit(
            c_red(f"Could not read audit file: {DATA_FILE}") + f"\n{exc}"
        ) from exc
    if not isinstance(data, list):
        raise SystemExit(
            c_red(f"Refusing to overwrite non-list audit file: {DATA_FILE}")
            + "\nExpected a JSON array."
        )
    return data


def save_entries(entries):
    ensure_dirs()
    tmp = DATA_FILE.with_suffix(".json.tmp")
    with tmp.open("w", encoding="utf-8") as f:
        json.dump(entries, f, indent=2, ensure_ascii=False)
    tmp.replace(DATA_FILE)


# --------------------------------------------------------------------------- #
# Entry helpers
# --------------------------------------------------------------------------- #

def split_csv(value):
    if not value:
        return []
    return [item.strip() for item in value.split(",") if item.strip()]


def parse_date(entry):
    """Parse an entry's ISO date into a datetime; fall back to epoch."""
    raw = entry.get("date", "")
    try:
        # Handle trailing Z
        if raw.endswith("Z"):
            raw = raw[:-1] + "+00:00"
        d = dt.datetime.fromisoformat(raw)
        if d.tzinfo is not None:
            d = d.astimezone().replace(tzinfo=None)
        return d
    except (ValueError, TypeError):
        return dt.datetime.min


def iso_week_key(d):
    """Return (iso_year, iso_week) for a datetime."""
    iso = d.isocalendar()
    return (iso[0], iso[1])


def week_bounds_for_offset(offset):
    """Return (start, end) datetimes for the week `offset` weeks ago (0=current)."""
    today = dt.datetime.now()
    monday = today - dt.timedelta(days=today.weekday())
    monday = monday.replace(hour=0, minute=0, second=0, microsecond=0)
    start = monday - dt.timedelta(weeks=offset)
    end = start + dt.timedelta(weeks=1)
    return start, end


def build_entry(project, task, impact, skills, commit_hash, doc_link,
                tags, repo, source, date=None):
    remote_url = git_remote_url() if in_git_repo() else None

    if commit_hash is None and in_git_repo():
        commit_hash = git_head()

    if repo is None and remote_url:
        repo = parse_repo_name(remote_url)

    commit_url = build_commit_url(remote_url, commit_hash) if commit_hash else None

    return {
        "id": str(uuid.uuid4()),
        "date": (date or dt.datetime.now()).isoformat(),
        "project": project or "",
        "task": task or "",
        "impact": impact or "",
        "skills": skills or [],
        "commit_hash": commit_hash,
        "commit_url": commit_url,
        "doc_link": doc_link,
        "repo": repo,
        "tags": tags or [],
        "source": source or SOURCE_DEFAULT,
    }


def add_entry(entry):
    entries = load_entries()
    entries.append(entry)
    save_entries(entries)


# --------------------------------------------------------------------------- #
# Commands
# --------------------------------------------------------------------------- #

def prompt(label, default=None):
    suffix = f" [{default}]" if default else ""
    try:
        value = input(f"{c_cyan(label)}{suffix}: ").strip()
    except EOFError:
        return default or ""
    if not value and default is not None:
        return default
    return value


def cmd_log(args):
    if args.quick is not None:
        task = args.quick
        commit_hash = args.commit
        entry = build_entry(
            project=args.project,
            task=task,
            impact=args.impact,
            skills=split_csv(args.skills),
            commit_hash=commit_hash,
            doc_link=args.doc,
            tags=split_csv(args.tags),
            repo=None,
            source=SOURCE_DEFAULT,
        )
        add_entry(entry)
        print(c_green(f"Logged accomplishment {c_bold(entry['id'])}"))
        if entry["commit_url"]:
            print(c_dim(f"  commit: {entry['commit_url']}"))
        return 0

    # Interactive wizard
    print(c_bold("Log a new accomplishment"))
    print(c_dim("Press Enter to accept defaults shown in brackets.\n"))

    detected_commit = git_head() if in_git_repo() else None
    detected_repo = parse_repo_name(git_remote_url()) if in_git_repo() else None

    project = prompt("Project", detected_repo.split("/")[-1] if detected_repo else None)
    task = prompt("Task description")
    impact = prompt("Impact / metrics")
    skills = split_csv(prompt("Skills (comma-separated)"))
    commit_hash = prompt("Commit hash", detected_commit) if detected_commit else \
        prompt("Commit hash") or None
    if not commit_hash:
        commit_hash = None
    doc_link = prompt("Doc link (optional)") or None
    tags = split_csv(prompt("Tags (comma-separated, optional)"))

    entry = build_entry(
        project=project,
        task=task,
        impact=impact,
        skills=skills,
        commit_hash=commit_hash,
        doc_link=doc_link,
        tags=tags,
        repo=detected_repo,
        source=SOURCE_DEFAULT,
    )
    add_entry(entry)
    print()
    print(c_green(f"Logged accomplishment {c_bold(entry['id'])}"))
    if entry["commit_url"]:
        print(c_dim(f"  commit: {entry['commit_url']}"))
    return 0


def _truncate(text, width):
    text = text.replace("\n", " ")
    if len(text) <= width:
        return text
    return text[: width - 1] + "…"


def cmd_list(args):
    entries = load_entries()

    if args.project:
        entries = [e for e in entries if e.get("project") == args.project]

    if args.week:
        start, end = week_bounds_for_offset(0)
        entries = [e for e in entries if start <= parse_date(e) < end]

    entries.sort(key=parse_date)
    if args.last and args.last > 0:
        entries = entries[-args.last:]

    if not entries:
        print(c_dim("No entries found."))
        return 0

    date_w, proj_w, task_w, skills_w = 16, 18, 40, 30
    print(c_bold(f"{'Date':<{date_w}} {'Project':<{proj_w}} "
                 f"{'Task':<{task_w}} {'Skills':<{skills_w}}"))
    print(c_dim("-" * (date_w + proj_w + task_w + skills_w + 3)))

    for e in entries:
        d = parse_date(e)
        date_s = d.strftime("%Y-%m-%d %H:%M") if d != dt.datetime.min else "?"
        proj = _truncate(e.get("project", ""), proj_w)
        task = _truncate(e.get("task", ""), task_w)
        skills = _truncate(", ".join(e.get("skills", [])), skills_w)
        print(f"{date_s:<{date_w}} {c_blue(f'{proj:<{proj_w}}')} "
              f"{task:<{task_w}} {c_dim(f'{skills:<{skills_w}}')}")
    return 0


def _commit_md(entry):
    h = entry.get("commit_hash")
    if not h:
        return ""
    short = h[:7]
    url = entry.get("commit_url")
    if url:
        return f" [commit: [`{short}`]({url})]"
    return f" [commit: `{short}`]"


def _doc_md(entry):
    link = entry.get("doc_link")
    if not link:
        return ""
    return f" [[docs]({link})]"


def render_summary(entries, year, week, project_filter):
    projects = sorted({e.get("project", "") or "(none)" for e in entries})
    now = dt.datetime.now().strftime("%Y-%m-%d %H:%M")

    lines = []
    lines.append(f"# Weekly Accomplishments — Week {week:02d}, {year}")
    proj_list = ", ".join(projects) if projects else "—"
    lines.append(
        f"> Generated: {now}  |  Projects: {proj_list}  |  "
        f"Tasks Completed: {len(entries)}"
    )
    lines.append("")

    if project_filter:
        lines.append(f"_Filtered to project: **{project_filter}**_")
        lines.append("")

    # Group by project
    by_project = {}
    for e in entries:
        by_project.setdefault(e.get("project", "") or "(none)", []).append(e)

    for proj in sorted(by_project):
        lines.append(f"## {proj}")
        for e in sorted(by_project[proj], key=parse_date):
            task = e.get("task", "").strip() or "(untitled task)"
            impact = e.get("impact", "").strip()
            skills = e.get("skills", [])
            piece = f"- **{task}**"
            if impact:
                piece += f" — {impact}"
            if skills:
                piece += f" *(Skills: {', '.join(skills)})*"
            piece += _commit_md(e)
            piece += _doc_md(e)
            lines.append(piece)
        lines.append("")

    # Skills table
    skill_counts = Counter()
    for e in entries:
        for s in e.get("skills", []):
            skill_counts[s] += 1

    lines.append("## Skills Applied This Week")
    if skill_counts:
        lines.append("| Skill | Times Used |")
        lines.append("|-------|------------|")
        for skill, count in skill_counts.most_common():
            lines.append(f"| {skill} | {count} |")
    else:
        lines.append("_No skills recorded._")
    lines.append("")

    # Impact summary
    lines.append("## Impact Summary")
    impacts = [e.get("impact", "").strip() for e in entries if e.get("impact", "").strip()]
    if impacts:
        for imp in impacts:
            lines.append(f"- {imp}")
    else:
        lines.append("_No impact metrics recorded._")
    lines.append("")

    return "\n".join(lines)


def cmd_summary(args):
    entries = load_entries()
    start, end = week_bounds_for_offset(args.week)
    week_entries = [e for e in entries if start <= parse_date(e) < end]

    if args.project:
        week_entries = [e for e in week_entries if e.get("project") == args.project]

    iso = start.isocalendar()
    year, week = iso[0], iso[1]

    markdown = render_summary(week_entries, year, week, args.project)

    # Always write to the auto summary file
    ensure_dirs()
    auto_path = SUMMARY_DIR / f"week-{year}-W{week:02d}.md"
    auto_path.write_text(markdown, encoding="utf-8")

    if args.output:
        out_path = Path(args.output).expanduser()
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(markdown, encoding="utf-8")
        print(c_green(f"Summary written to {out_path}"))
        print(c_dim(f"Also saved to {auto_path}"))
    else:
        print(markdown)
        print(c_dim(f"\n(Saved to {auto_path})"), file=sys.stderr)
    return 0


def cmd_export(args):
    entries = load_entries()

    if not args.all:
        start, end = week_bounds_for_offset(args.week)
        entries = [e for e in entries if start <= parse_date(e) < end]

    entries.sort(key=parse_date)

    fields = ["id", "date", "project", "task", "impact", "skills",
              "commit_hash", "commit_url", "doc_link", "repo", "tags", "source"]

    buf = io.StringIO()
    writer = csv.DictWriter(buf, fieldnames=fields, extrasaction="ignore")
    writer.writeheader()
    for e in entries:
        row = dict(e)
        row["skills"] = ", ".join(e.get("skills", []))
        row["tags"] = ", ".join(e.get("tags", []))
        writer.writerow(row)

    content = buf.getvalue()

    if args.output:
        out_path = Path(args.output).expanduser()
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(content, encoding="utf-8")
        print(c_green(f"Exported {len(entries)} entries to {out_path}"))
    else:
        sys.stdout.write(content)
    return 0


def cmd_git_hook(args):
    if not in_git_repo():
        print(c_red("Not inside a git repository."), file=sys.stderr)
        return 1

    git_dir = _git(["rev-parse", "--git-dir"])
    if not git_dir:
        print(c_red("Could not locate .git directory."), file=sys.stderr)
        return 1

    hooks_dir = Path(git_dir) / "hooks"
    hooks_dir.mkdir(parents=True, exist_ok=True)
    hook_path = hooks_dir / "post-commit"

    repo_name = parse_repo_name(git_remote_url()) or "unknown"
    repo_short = repo_name.split("/")[-1]
    track_bin = str(Path(__file__).resolve().parent / "track")

    hook = f"""#!/usr/bin/env bash
# Installed by `track git-hook`.
# Logs each commit as an accomplishment. Customize the task text below.
HASH=$(git log -1 --format=%H)
SUBJECT=$(git log -1 --format=%s)
"{track_bin}" log --quick "$SUBJECT" \\
  --project "{repo_short}" \\
  --commit "$HASH" || true
"""

    if hook_path.exists():
        backup = hook_path.with_suffix(".backup")
        hook_path.replace(backup)
        print(c_yellow(f"Existing post-commit hook backed up to {backup}"))

    hook_path.write_text(hook, encoding="utf-8")
    hook_path.chmod(0o755)

    print(c_green(f"Installed post-commit hook at {hook_path}"))
    print()
    print(c_bold("Customize:"))
    print(f"  Edit {hook_path} to change the task description, add")
    print("  --impact, --skills, or --tags flags as you like.")
    print(c_dim(f"  Disable by removing or chmod -x {hook_path}"))
    return 0


def cmd_stats(args):
    entries = load_entries()
    total = len(entries)

    now = dt.datetime.now()
    week_start, week_end = week_bounds_for_offset(0)
    month_start = now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)

    this_week = sum(1 for e in entries if week_start <= parse_date(e) < week_end)
    this_month = sum(1 for e in entries if parse_date(e) >= month_start)

    skill_counts = Counter()
    project_counts = Counter()
    for e in entries:
        for s in e.get("skills", []):
            skill_counts[s] += 1
        proj = e.get("project", "") or "(none)"
        project_counts[proj] += 1

    print(c_bold("Accomplishment Stats"))
    print(c_dim("-" * 32))
    print(f"{'Total entries':<22}{c_green(str(total))}")
    print(f"{'This week':<22}{c_green(str(this_week))}")
    print(f"{'This month':<22}{c_green(str(this_month))}")
    print()

    print(c_bold("Top 5 Skills"))
    if skill_counts:
        for skill, count in skill_counts.most_common(5):
            print(f"  {c_cyan(f'{skill:<20}')} {count}")
    else:
        print(c_dim("  (none)"))
    print()

    print(c_bold("Top Projects"))
    if project_counts:
        for proj, count in project_counts.most_common(5):
            print(f"  {c_blue(f'{proj:<20}')} {count}")
    else:
        print(c_dim("  (none)"))
    return 0


# --------------------------------------------------------------------------- #
# CLI
# --------------------------------------------------------------------------- #

def build_parser():
    parser = argparse.ArgumentParser(
        prog="track",
        description="CLI-first accomplishment tracker for Computer-assisted work.",
    )
    sub = parser.add_subparsers(dest="command")

    # log
    p_log = sub.add_parser("log", help="Log a new accomplishment")
    p_log.add_argument("--quick", metavar="TASK",
                       help="Quick one-liner log with the given task description")
    p_log.add_argument("-p", "--project", help="Project name")
    p_log.add_argument("-i", "--impact", help="Impact / metrics")
    p_log.add_argument("-s", "--skills", help="Comma-separated skills")
    p_log.add_argument("-c", "--commit", help="Commit hash (auto-detected if omitted)")
    p_log.add_argument("-d", "--doc", help="Doc link")
    p_log.add_argument("-t", "--tags", help="Comma-separated tags")
    p_log.set_defaults(func=cmd_log)

    # list
    p_list = sub.add_parser("list", help="List recent entries")
    p_list.add_argument("--last", type=int, default=10, help="Show last N entries")
    p_list.add_argument("--project", help="Filter by project")
    p_list.add_argument("--week", action="store_true", help="Show current week only")
    p_list.set_defaults(func=cmd_list)

    # summary
    p_sum = sub.add_parser("summary", help="Generate a weekly markdown summary")
    p_sum.add_argument("--week", type=int, default=0,
                      help="Week offset (0=current, 1=last week, ...)")
    p_sum.add_argument("--project", help="Filter by project")
    p_sum.add_argument("--output", help="Write to this path")
    p_sum.set_defaults(func=cmd_summary)

    # export
    p_exp = sub.add_parser("export", help="Export entries to CSV")
    p_exp.add_argument("--week", type=int, default=0, help="Week offset to export")
    p_exp.add_argument("--all", action="store_true", help="Export all entries")
    p_exp.add_argument("--output", help="Write to this path")
    p_exp.set_defaults(func=cmd_export)

    # git-hook
    p_hook = sub.add_parser("git-hook", help="Install a post-commit git hook")
    p_hook.set_defaults(func=cmd_git_hook)

    # stats
    p_stats = sub.add_parser("stats", help="Show statistics")
    p_stats.set_defaults(func=cmd_stats)

    return parser


def main(argv=None):
    C.init()
    parser = build_parser()
    args = parser.parse_args(argv)
    if not getattr(args, "command", None):
        parser.print_help()
        return 0
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
