# Workflow Hardening Handoff — 2026-11-14

## Scope and release hold

Validation workflows now default to `contents: read`; every checkout disables
persisted credentials. Package publication, image promotion, and signing
permissions are scoped to release jobs. Their only candidate source is a push
to `refs/heads/main` in `mirrornode/MIRRORNODE-CORE-HUB`, and each privileged
job also has a literal `false` condition. Thus even a trusted main push cannot
run a privileged release job. Pull requests (same-repository or fork), fork
pushes, `develop`, other refs, and manual dispatch do not pass the source
filters.

The existing OSIRIS and platform push triggers still include `main` and
`develop`; only `main` is retained as a potential privileged ref. No automatic
trigger was added. The sole `workflow_dispatch` trigger remains on the
Lucian validation-only workflow. No in-repository caller of
`reusable-runtime-release.yml` exists; any future caller must grant permissions
at its own call site because a reusable workflow cannot elevate caller
permissions.

The OSIRIS and platform runtime validators currently emit `ready=false` because
the Dockerfiles and compose surfaces are absent. Their dependent release,
integration, and dossier jobs therefore do not produce release evidence. When
a separately reviewed release path is ever authorized, the dossier jobs only
upload artifacts for review; they do not sign, commit, push, or update canon
indexes.

**Required Operator decision:** publication and signing authority, the trusted
source/ref policy, and any explicit release clearance remain unresolved.
Changing the literal default-deny conditions requires a separate Operator
decision and independent exact-head review; this handoff does not authorize
that change. No provider-side approval or protection is asserted.

## Permission and event boundary

Before: most audit and validation workflows had no explicit permission
ceiling; the Lucian validator already declared `contents: read`. Checkouts
persisted credentials. OSIRIS, platform, and reusable release workflows granted
`contents: write`, `packages: write`, and `id-token: write` at workflow scope.
Existing release jobs could publish on pushes to `develop` as well as `main` in
OSIRIS and platform workflows. Platform and OSIRIS release paths could commit
and push dossier/canonical records, with GPG secrets available to those jobs.

After: all seven tracked workflows explicitly default to `contents: read`.
Validation jobs have no write or OIDC scopes; the platform and reusable
integration jobs receive only `packages: read` for test-image pulls. Required
package-write/OIDC grants exist only on the release jobs, which are limited to
the canonical repository's main push and remain hard-disabled. No workflow
contains direct `git add`, `git commit`, or `git push`; generated dossiers are
unsigned artifacts, not repository updates. No `pull_request_target` or
`workflow_run` trigger was introduced.

The GitHub Actions API also lists a “Hermes Truth Gate” workflow record, but
the main branch's `.github/workflows` directory contains only the seven files
below and the listed Hermes file is not available from repository contents.
It was not changed.

## Changed files

- `.github/workflows/audit.yml`
- `.github/workflows/canon-gate.yml`
- `.github/workflows/lucian-release.yml`
- `.github/workflows/mirrornode-platform-release.yml`
- `.github/workflows/osiris-release.yml`
- `.github/workflows/platform-audit.yml`
- `.github/workflows/reusable-runtime-release.yml`
- `tests/test_workflow_hardening.py`
- `docs/verification/WORKFLOW_HARDENING_HANDOFF_2026-11-14.md`

The Python Lint check name and existing validation job names were retained.
The OSIRIS “Verify Promote Publish Dossier” job is now “Promote Release Image”
with a separate dossier-artifact job. Platform “Build • Sign • Test” was split
into “Build • Sign” and “Integration Tests”; the dossier/index job is now
artifact-only. Required-check consumers may need to account for those
unavoidable job-name changes.

## Validation evidence

- `python -m unittest -v tests/test_workflow_hardening.py tests/test_canon_gate.py`
  — 24 tests passed, including trusted-main candidate, same-repository PR,
  fork PR/push, untrusted ref, and manual-trigger cases.
- PyYAML `BaseLoader` parsed all seven local workflow YAML files.
- `ruff check . --ignore E501` — exit 1, 144 findings. The unmodified commit
  also had 144 findings; exact normalized comparison found zero additions or
  removals. These pre-existing Python findings remain intentionally unfixed.
- A disposable `/tmp` fixture containing an unused import was rejected by the
  same Ruff version/configuration with exit 1.
- `yamllint -f parsable .github/workflows/*.yml` — exit 1; 55 errors and 14
  warnings versus 71 errors and 14 warnings on the original workflows. The
  comparison found no new finding signatures.
- `actionlint` and `zizmor` were unavailable. No release workflow was invoked
  and no credentials were supplied.
- Historical failed OSIRIS run `25128867516` has a failed “Verify Charters”
  job; GitHub returned HTTP 410 when its logs were requested, so the cause
  could not be verified.

## Rollback and out-of-scope items

Rollback is a separately reviewed revert of this hardening change. Because a
revert restores the former broader permissions and repository-write behavior,
it must not be used to resume publication without the required Operator
decision and a fresh review.

Branch protections, environments, GitHub App installation, deployment,
publication, runtime changes, canon ratification, and merge remain out of
scope. This change does not inspect or alter repository settings or secrets,
and does not claim that provider-side controls enforce the workflow gates.
