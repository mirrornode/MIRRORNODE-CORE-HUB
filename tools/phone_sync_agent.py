#!/usr/bin/env python3
"""
MIRRORNODE Phone Sync Agent — Local Fallback
Watches iCloud Drive mirrornode-notes/ folder and auto-commits
new .md and .m4a files to mirrornode-docs/session-notes/ on GitHub.

Use this if Toolhouse is unavailable. Production path: tools/toolhouse/mirror-phone-sync/

Requires:
    pip install watchdog openai-whisper

Usage:
    python tools/phone_sync_agent.py
"""

import time
import subprocess
import whisper
from pathlib import Path
from datetime import date
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

WATCH_DIR = Path.home() / "Library/Mobile Documents/com~apple~CloudDocs/mirrornode-notes"
REPO_DIR  = Path.home() / "path/to/mirrornode-docs"  # UPDATE THIS
TARGET    = REPO_DIR / "session-notes"
MODEL     = whisper.load_model("base")

HEADER = """---
Date: {date}
Source: Phone
Status: Pending-Integration
---

"""


def commit_file(dest: Path, filename: str):
    subprocess.run(["git", "-C", str(REPO_DIR), "add", str(dest)], check=True)
    subprocess.run(["git", "-C", str(REPO_DIR), "commit",
                    "-m", f"sync: phone note {filename} [mirror-phone-sync auto]"], check=True)
    subprocess.run(["git", "-C", str(REPO_DIR), "push"], check=True)
    print(f"✅ Committed {filename}")


class NoteHandler(FileSystemEventHandler):
    def on_created(self, event):
        src = Path(event.src_path)

        if src.suffix == ".md":
            stem = src.stem if src.stem.startswith("20") else f"{date.today()}_{src.stem}"
            dest = TARGET / f"{stem}.md"
            content = HEADER.format(date=date.today()) + src.read_text()
            dest.write_text(content)
            commit_file(dest, dest.name)

        elif src.suffix == ".m4a":
            print(f"🎙 Transcribing {src.name}...")
            result = MODEL.transcribe(str(src))
            stem = src.stem if src.stem.startswith("20") else f"{date.today()}_{src.stem}"
            dest = TARGET / f"{stem}.md"
            content = HEADER.format(date=date.today()) + f"# {src.stem}\n\n" + result["text"]
            dest.write_text(content)
            commit_file(dest, dest.name)


if __name__ == "__main__":
    TARGET.mkdir(parents=True, exist_ok=True)
    observer = Observer()
    observer.schedule(NoteHandler(), str(WATCH_DIR), recursive=False)
    observer.start()
    print(f"👁  Watching {WATCH_DIR}")
    print(f"📁  Committing to {TARGET}")
    try:
        while True:
            time.sleep(5)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
