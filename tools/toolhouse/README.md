# MIRRORNODE Toolhouse Agent Suite

**Authority:** Operator (Sean Malm)  
**Status:** Active  
**Last Updated:** 2026-06-23

---

## Overview

This directory contains all Toolhouse agent definitions for the MIRRORNODE ecosystem.
These agents run on hosted Toolhouse infrastructure and connect to GitHub, Notion, Slack,
and the MIRRORNODE RAG knowledge store via MCP servers.

No local process needs to run 24/7. All agents are deployed via `th deploy` and
scheduled or webhook-triggered from the Toolhouse cloud.

---

## Agents

| Agent | Schedule | Purpose |
|-------|----------|---------|
| `mirror-phone-sync` | Hourly | Phone notes + voice memos → `mirrornode-docs/session-notes/` |
| `mirror-notion-sync` | Daily 7am | Notion page exports → `mirrornode-docs/notion-exports/` |
| `mirror-rag-indexer` | Hourly +30m | Ingest new `.md` files into RAG knowledge store |
| `mirror-repo-auditor` | Weekly Mon 9am | Audit `REPO_MAP.md` vs live GitHub org, auto-update |
| `mirror-canon-watcher` | Daily 6am | Check charter `.sig` files, INDEX.md coverage, status freshness |
| `mirror-session-brief` | Daily 8am | Generate daily brief from RAG + recent commits → Slack |

---

## MCP Servers Required

| MCP Server | Provider | Used By |
|------------|----------|---------|
| GitHub MCP | Smithery | All agents |
| Notion MCP | Pipedream or Smithery | mirror-notion-sync |
| Slack MCP | Smithery | mirror-canon-watcher, mirror-session-brief |
| Whisper | Toolhouse native | mirror-phone-sync |
| Toolhouse RAG | Toolhouse native | mirror-rag-indexer, mirror-session-brief |

---

## Setup

### 1. Install Toolhouse CLI
```bash
npm install -g @toolhouseai/cli
th login
```

### 2. Configure MCP servers in Toolhouse Agent Studio
- Add your GitHub MCP remote URL (Smithery)
- Add Notion MCP via Pipedream or Smithery
- Add Slack MCP via Smithery
- Enable Toolhouse RAG store named `mirrornode-rag`

### 3. Set environment variables
```bash
th env set GITHUB_MCP_URL=https://server.smithery.ai/@your-github-mcp
th env set NOTION_MCP_URL=https://mcp.pipedream.net/your-token/notion
th env set SLACK_MCP_URL=https://server.smithery.ai/@smithery-ai/slack/mcp?api_key=YOUR_KEY
th env set SLACK_CANON_CHANNEL=#mirrornode-canon
th env set SLACK_DAILY_CHANNEL=#mirrornode-daily
th env set ICLOUD_WATCH_PATH=~/Library/Mobile\ Documents/com~apple~CloudDocs/mirrornode-notes
```

### 4. Deploy all agents
```bash
cd tools/toolhouse
for dir in mirror-*/; do
  echo "Deploying $dir..."
  th deploy $dir
done
```

### 5. Phone setup (one-time, 2 min)
- Enable iCloud Drive on iPhone
- Create folder: `iCloud Drive/mirrornode-notes/`
- Drop any `.md` or `.m4a` file there — `mirror-phone-sync` picks it up within the hour

---

## RAG Store

The `mirrornode-rag` store is populated by `mirror-rag-indexer` and queried by
`mirror-session-brief`. To manually add content:
```bash
th rag add mirrornode-rag --file path/to/file.md
```

To query the store directly:
```bash
th rag query mirrornode-rag "what did we decide about Thoth persistence?"
```

---

## Local Fallback

If Toolhouse is unavailable, `tools/phone_sync_agent.py` provides a local
watchdog-based equivalent for `mirror-phone-sync`. See that file for usage.

---

*All agents are subject to the `emit_audit()` contract defined in `canon/contracts/`.*
