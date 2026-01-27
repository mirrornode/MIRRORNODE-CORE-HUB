# AGENT PROTOCOL v1.0

## Truth Sources (Priority Order)
1. canon/charters/
2. state/repos.json
3. state/audit-summary.txt
4. artifacts/
5. schemas/
6. examples/

## Agent Coordination
- All agents MUST `git pull origin main` before execution.
- Charter violations MUST halt execution and emit a violation artifact.
- State updates MUST be atomic commits.
- Artifacts MUST include provenance metadata.

## Update Protocol
git pull origin main
git add state/ artifacts/
git commit -m "[AGENT_NAME] <action>: <description>"
git push origin main
