# `track` — CLI-First Accomplishment Tracker

`track` logs completed Computer (Perplexity AI Computer-assisted) tasks into a
structured JSON file and generates polished weekly markdown summaries, CSV
exports, and statistics. It is a single, dependency-free Python 3 script —
nothing to install beyond having `python3` on your `PATH`.

Entries in `accomplishments.json` serve as the **audit trail for
Computer-assisted sessions** in the MIRRORNODE workflow, cross-referenced by
commit hash so any logged task can be traced back to the exact code change that
produced it.

---

## Installation

The tool lives at `tools/track.py` with a shell wrapper at `tools/track`.

**Option A — add `tools/` to your `PATH`:**

```bash
export PATH="$PATH:/path/to/MIRRORNODE-CORE-HUB/tools"
track --help
```

**Option B — symlink into a directory already on your `PATH`:**

```bash
ln -s "$(pwd)/tools/track" ~/.local/bin/track
```

**Option C — call it directly:**

```bash
./tools/track --help
# or
python3 tools/track.py --help
```

No external dependencies — pure Python 3 standard library.

### Data location

All state lives under `~/.mirrornode/` (created automatically):

| Path | Purpose |
|------|---------|
| `~/.mirrornode/accomplishments.json` | All logged entries (the audit trail) |
| `~/.mirrornode/summaries/week-YYYY-WNN.md` | Auto-saved weekly summaries |

### Color

Output is colorized with ANSI codes when writing to a terminal. Set the
`NO_COLOR` environment variable (any value) to disable, e.g. `NO_COLOR=1 track list`.
Color is also disabled automatically when output is piped or redirected.

---

## Commands

### `track log` — interactive wizard

Prompts for project, task, impact, skills, commit hash, doc link, and tags.
When run inside a git repo it pre-fills the commit hash from `HEAD` and the
project from the repo name.

```bash
track log
```

### `track log --quick` — one-liner

```bash
track log --quick "Centralized agent manifest in lib/agents.ts" \
  --project mirrornode-core-hub \
  --impact "Single source of truth; removed 3 duplicate definitions" \
  --skills "TypeScript,Next.js" \
  --tags "refactor,canon"
```

| Flag | Meaning |
|------|---------|
| `-p`, `--project` | Project name |
| `-i`, `--impact` | Impact / metrics |
| `-s`, `--skills` | Comma-separated skills |
| `-c`, `--commit` | Commit hash (auto-detected from `HEAD` if omitted) |
| `-d`, `--doc` | Doc link (URL or path) |
| `-t`, `--tags` | Comma-separated tags |

### `track list` — recent entries

```bash
track list                       # last 10
track list --last 25             # last 25
track list --project osiris      # filter by project
track list --week                # current week only
```

Shows aligned columns: **Date · Project · Task (truncated) · Skills**.

### `track summary` — weekly markdown

```bash
track summary                    # current week → stdout (and auto-saved)
track summary --week 1           # last week
track summary --project osiris   # filter to one project
track summary --output report.md # also write to a chosen path
```

The summary is **always** auto-saved to
`~/.mirrornode/summaries/week-YYYY-WNN.md`. `--week N` selects the week offset
(`0` = current, `1` = last week, …).

### `track export` — CSV

```bash
track export                          # current week → stdout
track export --week 2                 # a specific week offset
track export --all --output all.csv   # everything, to a file
```

### `track git-hook` — install post-commit hook

Run inside a git repo to install `.git/hooks/post-commit` that logs every
commit automatically (using the commit subject as the task, the repo name as
the project, and the commit hash). An existing hook is backed up to
`post-commit.backup`.

```bash
track git-hook
```

Edit the generated hook to add `--impact`, `--skills`, or `--tags`. Disable it
by removing the file or `chmod -x .git/hooks/post-commit`.

### `track stats` — statistics

```bash
track stats
```

Prints total entries, counts for this week/month, the top 5 skills by
frequency, and the top projects by entry count.

---

## GitHub Integration

When an entry has a commit hash (provided via `--commit` or auto-detected from
`HEAD`), `track` parses the `origin` remote and builds a commit URL:

- SSH remotes — `git@github.com:org/repo.git`
- HTTPS remotes — `https://github.com/org/repo.git`

both become `https://github.com/org/repo/commit/<hash>`, stored as
`commit_url` on the entry. In weekly summaries the commit renders as a markdown
link:

```markdown
[commit: [`abc1234`](https://github.com/org/repo/commit/abc1234)]
```

The same parser is used for any host (e.g. an internal GitHub Enterprise host),
so commit URLs always point at the correct origin.

---

## JSON Schema Reference

Each entry in `~/.mirrornode/accomplishments.json` is an object:

| Field | Type | Notes |
|-------|------|-------|
| `id` | string | Auto-generated UUID v4 |
| `date` | string | ISO 8601 datetime (defaults to now) |
| `project` | string | Project name |
| `task` | string | Task description |
| `impact` | string | Impact / metrics |
| `skills` | string[] | Skills used |
| `commit_hash` | string \| null | Auto-detected from `HEAD` when in a repo |
| `commit_url` | string \| null | Derived GitHub URL for the commit |
| `doc_link` | string \| null | URL or path to related docs |
| `repo` | string \| null | `org/repo`, auto-detected from `origin` |
| `tags` | string[] | Optional tags |
| `source` | string | Defaults to `"computer"` (AI-assisted) |

Example:

```json
{
  "id": "c0d89b31-f1c3-4c87-9ce2-f084a3039050",
  "date": "2026-06-22T21:04:20.743432",
  "project": "mirrornode-core-hub",
  "task": "Centralized agent manifest in lib/agents.ts",
  "impact": "Single source of truth; removed 3 duplicate definitions",
  "skills": ["TypeScript", "Next.js"],
  "commit_hash": "26c64584692f0bf353bca1b29ab10ccfeeb0069b",
  "commit_url": "https://github.com/mirrornode/MIRRORNODE-CORE-HUB/commit/26c64584692f0bf353bca1b29ab10ccfeeb0069b",
  "doc_link": null,
  "repo": "mirrornode/MIRRORNODE-CORE-HUB",
  "tags": ["refactor", "canon"],
  "source": "computer"
}
```

---

## Integration with the MIRRORNODE Documentation Workflow

`accomplishments.json` is the **audit trail** for Computer-assisted sessions.
Every entry is keyed to a commit hash, so a logged accomplishment can be
cross-referenced against the canonical git history and the canon documentation
in this repo. Recommended workflow:

1. Install the post-commit hook (`track git-hook`) so each change is logged with
   its commit hash as you work.
2. Enrich notable entries with `track log --quick … --impact … --skills …` to
   capture *what improved*, not just *what changed*.
3. At the end of the week, run `track summary` — the generated markdown is ready
   to drop into a performance review, status update, or canon progress report,
   with every claim linked back to a verifiable commit.

Because the `source` field defaults to `"computer"`, the trail clearly marks
which work was AI-assisted, supporting the repo's "documentation must reflect
real code paths only" principle.
