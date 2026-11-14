import re
import unittest
from pathlib import Path

WORKFLOWS = Path(__file__).resolve().parents[1] / ".github" / "workflows"
RELEASE_JOBS = {
    "osiris-release.yml": {
        "build-and-push": {"packages: write", "id-token: write"},
        "promote": {"packages: write"},
    },
    "mirrornode-platform-release.yml": {
        "build-and-push": {"packages: write", "id-token: write"},
        "promote": {"packages: write"},
    },
    "reusable-runtime-release.yml": {
        "build-and-sign": {"packages: write", "id-token: write"},
    },
}
SECRET_BEARING_JOBS = {
    "osiris-release.yml": {"build-and-push"},
    "mirrornode-platform-release.yml": {"build-and-push", "integration-tests"},
    "reusable-runtime-release.yml": {"build-and-sign", "integration-tests"},
}
CANONICAL_REPOSITORY = "mirrornode/MIRRORNODE-CORE-HUB"


def workflow_text(name):
    return (WORKFLOWS / name).read_text()


def job_block(text, job_name):
    match = re.search(rf"^  {re.escape(job_name)}:\s*$", text, re.MULTILINE)
    if not match:
        raise AssertionError(f"Missing job: {job_name}")
    remainder = text[match.end() :]
    next_job = re.search(r"^  [A-Za-z0-9_-]+:\s*$", remainder, re.MULTILINE)
    return remainder[: next_job.start()] if next_job else remainder


def job_condition(block):
    lines = block.splitlines()
    for index, line in enumerate(lines):
        if not re.match(r"^\s+if:", line):
            continue
        value = line.split("if:", 1)[1].strip()
        if value in (">-", ">"):
            expression = []
            for continuation in lines[index + 1 :]:
                if continuation.strip() and len(continuation) - len(continuation.lstrip()) <= 4:
                    break
                expression.append(continuation.strip())
            return " ".join(expression)
        return value
    return ""


def trusted_source(repository, event, ref):
    return (
        repository == CANONICAL_REPOSITORY
        and event == "push"
        and ref == "refs/heads/main"
    )


class WorkflowHardeningTests(unittest.TestCase):
    def test_audit_lint_is_unsuppressed_and_keeps_check_name(self):
        text = workflow_text("audit.yml")
        lint = job_block(text, "lint")
        self.assertRegex(text, r"(?m)^    name: Python Lint$")
        self.assertRegex(lint, r"(?m)^\s+run: ruff check \. --ignore E501$")
        self.assertNotRegex(lint, r"\|\|\s*true|continue-on-error")
        audit = job_block(text, "audit")
        self.assertIn('event_type="execution"', audit)
        self.assertIn('"event": os.environ.get("GITHUB_EVENT_NAME")', audit)

    def test_all_workflows_default_to_read_only_contents(self):
        for path in sorted(WORKFLOWS.glob("*.yml")):
            with self.subTest(workflow=path.name):
                text = path.read_text()
                self.assertRegex(
                    text,
                    r"(?m)^permissions:\n(?:^  [^\n]*\n)*^  contents: read$",
                )
                self.assertNotRegex(text, r"(?m)^\s+contents: write$")

    def test_every_checkout_disables_persisted_credentials(self):
        for path in sorted(WORKFLOWS.glob("*.yml")):
            lines = path.read_text().splitlines()
            checkout_indexes = [
                index
                for index, line in enumerate(lines)
                if re.match(r"\s*uses:\s*actions/checkout@", line)
            ]
            for index in checkout_indexes:
                indent = len(lines[index]) - len(lines[index].lstrip())
                step_lines = [lines[index]]
                for line in lines[index + 1 :]:
                    if line.strip():
                        line_indent = len(line) - len(line.lstrip())
                        if line_indent < indent:
                            break
                        if line_indent == indent and line.lstrip().startswith("- "):
                            break
                    step_lines.append(line)
                with self.subTest(workflow=path.name, step=index):
                    self.assertIn("persist-credentials: false", "\n".join(step_lines))

    def test_write_and_oidc_permissions_are_scoped_to_release_jobs(self):
        for workflow, jobs in RELEASE_JOBS.items():
            text = workflow_text(workflow)
            for name, permissions in jobs.items():
                with self.subTest(workflow=workflow, job=name):
                    block = job_block(text, name)
                    for permission in permissions:
                        self.assertRegex(block, rf"(?m)^\s+{re.escape(permission)}$")
                    condition = job_condition(block)
                    self.assertIn(f"github.repository == '{CANONICAL_REPOSITORY}'", condition)
                    self.assertIn("github.event_name == 'push'", condition)
                    self.assertIn("github.ref == 'refs/heads/main'", condition)
                    self.assertRegex(condition, r"\bfalse\b")

        for path in sorted(WORKFLOWS.glob("*.yml")):
            text = path.read_text()
            for permission in ("packages: write", "id-token: write"):
                for match in re.finditer(rf"(?m)^\s+{re.escape(permission)}$", text):
                    preceding = text[: match.start()]
                    job_match = list(re.finditer(r"(?m)^  ([A-Za-z0-9_-]+):\s*$", preceding))
                    self.assertTrue(job_match, f"{permission} is not job-scoped in {path.name}")
                    current_job = job_match[-1].group(1)
                    self.assertIn(current_job, RELEASE_JOBS.get(path.name, {}))

    def test_release_credentials_are_not_in_validation_jobs(self):
        for path in sorted(WORKFLOWS.glob("*.yml")):
            text = path.read_text()
            for match in re.finditer(r"(?m)^\s*password:\s*\$\{\{\s*secrets\.GITHUB_TOKEN\s*\}\}", text):
                preceding = text[: match.start()]
                job_match = list(re.finditer(r"(?m)^  ([A-Za-z0-9_-]+):\s*$", preceding))
                self.assertTrue(job_match, f"Token use is not job-scoped in {path.name}")
                current_job = job_match[-1].group(1)
                self.assertIn(current_job, SECRET_BEARING_JOBS.get(path.name, set()))

        all_workflows = "\n".join(path.read_text() for path in WORKFLOWS.glob("*.yml"))
        for forbidden_secret in ("GPG_PRIVATE_KEY", "GPG_PASSPHRASE", "COSIGN_KEY"):
            self.assertEqual(all_workflows.count(forbidden_secret), 0)

    def test_release_gate_event_and_ref_cases(self):
        cases = [
            ("trusted push", CANONICAL_REPOSITORY, "push", "refs/heads/main", True),
            ("develop push", CANONICAL_REPOSITORY, "push", "refs/heads/develop", False),
            (
                "untrusted push",
                CANONICAL_REPOSITORY,
                "push",
                "refs/heads/feature/untrusted",
                False,
            ),
            (
                "same-repository PR",
                CANONICAL_REPOSITORY,
                "pull_request",
                "refs/pull/42/merge",
                False,
            ),
            (
                "fork PR",
                CANONICAL_REPOSITORY,
                "pull_request",
                "refs/pull/43/merge",
                False,
            ),
            (
                "fork push to main",
                "fork-owner/MIRRORNODE-CORE-HUB",
                "push",
                "refs/heads/main",
                False,
            ),
            (
                "manual trigger",
                CANONICAL_REPOSITORY,
                "workflow_dispatch",
                "refs/heads/main",
                False,
            ),
        ]
        for scenario, repository, event, ref, expected in cases:
            with self.subTest(scenario=scenario):
                self.assertEqual(trusted_source(repository, event, ref), expected)

        for workflow, jobs in RELEASE_JOBS.items():
            text = workflow_text(workflow)
            for name in jobs:
                condition = job_condition(job_block(text, name))
                for scenario, repository, event, ref, expected_source in cases:
                    source_allowed = trusted_source(repository, event, ref)
                    release_enabled = source_allowed and "false" not in condition.lower()
                    with self.subTest(
                        workflow=workflow,
                        job=name,
                        scenario=scenario,
                    ):
                        self.assertEqual(source_allowed, expected_source)
                        self.assertFalse(release_enabled)

        lucian = workflow_text("lucian-release.yml")
        self.assertRegex(lucian, r"(?m)^  workflow_dispatch:\s*$")

    def test_missing_runtime_surfaces_cannot_satisfy_release_gates(self):
        surfaces = (
            ("osiris-release.yml", "validate-runtime-surface", "build-and-push"),
            (
                "mirrornode-platform-release.yml",
                "validate-release-surface",
                "build-and-push",
            ),
            (
                "reusable-runtime-release.yml",
                "validate-runtime-surface",
                "build-and-sign",
            ),
        )
        for workflow, validator, release_job in surfaces:
            with self.subTest(workflow=workflow):
                text = workflow_text(workflow)
                self.assertIn("ready=false", job_block(text, validator))
                self.assertIn(
                    f"needs.{validator}.outputs.ready == 'true'",
                    job_condition(job_block(text, release_job)),
                )

    def test_package_push_steps_are_inside_default_denied_release_jobs(self):
        for workflow, jobs in RELEASE_JOBS.items():
            text = workflow_text(workflow)
            for pattern in (
                r"(?m)^\s*push:\s*true$",
                r"\bdocker push\b",
            ):
                for match in re.finditer(pattern, text):
                    preceding = text[: match.start()]
                    job_match = list(re.finditer(r"(?m)^  ([A-Za-z0-9_-]+):\s*$", preceding))
                    self.assertTrue(job_match, f"Package push is not job-scoped in {workflow}")
                    current_job = job_match[-1].group(1)
                    self.assertIn(current_job, jobs)
                    self.assertIn("false", job_condition(job_block(text, current_job)).lower())

    def test_dossiers_are_artifacts_not_repository_writes(self):
        all_workflows = "\n".join(path.read_text() for path in WORKFLOWS.glob("*.yml"))
        self.assertNotRegex(all_workflows, r"\bgit\s+(?:push|commit|add)\b")
        self.assertNotRegex(all_workflows, r"(?m)^\s*(?:pull_request_target|workflow_run):")
        self.assertIn("uses: actions/upload-artifact@v4", workflow_text("osiris-release.yml"))
        self.assertIn(
            "uses: actions/upload-artifact@v4",
            workflow_text("mirrornode-platform-release.yml"),
        )


if __name__ == "__main__":
    unittest.main()
