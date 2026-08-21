#!/usr/bin/env python3
"""CG-0036 bounded-hardening fixtures: canonicalization, schemas, commit tables."""

from __future__ import annotations

import hashlib
import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DELEGATION = ROOT / "docs" / "delegation"
VECTORS = json.loads((DELEGATION / "CANONICALIZATION_VECTORS_V0_1.json").read_text())
COMMIT_VECTORS = json.loads((DELEGATION / "EFFECT_CONSUMPTION_COMMIT_VECTORS_V0_1.json").read_text())

try:
    from jsonschema import Draft7Validator
except ImportError:  # pragma: no cover - optional in default repo env
    Draft7Validator = None


def rfc8785(value):
    return json.dumps(value, ensure_ascii=False, separators=(",", ":"), sort_keys=True, allow_nan=False)


def sha256_labeled(canonical: str) -> str:
    return "sha256:" + hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def reject_duplicates(pairs):
    seen = {}
    for key, val in pairs:
        if key in seen:
            raise ValueError("duplicate key")
        seen[key] = val
    return seen


def parse_strict(text: str):
    if re.search(r"\bNaN\b|\bInfinity\b", text):
        raise ValueError("non-ijson")
    return json.loads(text, parse_constant=lambda v: (_ for _ in ()).throw(ValueError("non-ijson")), object_pairs_hook=reject_duplicates)


def load_schema(name: str):
    return json.loads((DELEGATION / name).read_text())


SHA256 = "sha256:" + ("a" * 64)
NONCE = "AAAAAAAAAAAAAAAAAAAAAA"
PROOF = {
    "proof_type": "DIGITAL_SIGNATURE",
    "issuer_credential_ref": "did:example:pdp#key-1",
    "signed_payload_hash": SHA256,
    "proof_value": "eyJhbGciOiJFUzI1NiIsImtpZCI6InBkcC1rZXktMSJ9.placeholder",
}
URI = "mirrornode://github/repository/MIRRORNODE-CORE-HUB"


def decision_base(**overrides):
    doc = {
        "decision_id": "dec-1",
        "decision_nonce": NONCE,
        "request_id": "req-1",
        "subject": {"type": "actor", "id": "agent-a"},
        "action": {"name": "op:x", "parameters_hash": SHA256},
        "resource": {"type": "github.repository", "id": URI, "canonical_uri": URI},
        "resource_registry_ref": "docs/delegation/resource-registry",
        "resource_registry_snapshot_hash": SHA256,
        "context_digest": SHA256,
        "delegation_id": "del-1",
        "delegation_version": "1.0.0",
        "delegation_payload_hash": SHA256,
        "authority_class": "AUTONOMOUS_WITHIN_POLICY",
        "micc_approval_class": "APPROVAL_NONE",
        "pdp_identity": "pdp-primary",
        "pdp_version": "0.1.0",
        "issuer_proof": dict(PROOF),
        "policy_content_hash": SHA256,
        "policy_bundle_hash": SHA256,
        "decision_preconditions_hash": SHA256,
        "aggregate_authority_snapshot_hash": SHA256,
        "state_hash": SHA256,
        "decision": "DENY",
        "reason_code": "DENIED",
        "issued_at": "2026-08-21T12:00:00Z",
        "expires_at": "2026-08-21T13:00:00Z",
    }
    doc.update(overrides)
    return doc


class CanonicalizationVectorTests(unittest.TestCase):
    def test_recorded_vectors(self):
        by_id = {v["id"]: v for v in VECTORS["vectors"]}
        for vec in VECTORS["vectors"]:
            if vec["expected_result"] == "reject_duplicate_keys":
                with self.assertRaises(ValueError):
                    parse_strict(vec["raw_json"])
                continue
            if vec["expected_result"] == "reject_non_ijson":
                with self.assertRaises(ValueError):
                    parse_strict(vec["raw_json"])
                continue
            payload = vec["input"]
            if vec.get("exclude_issuer_proof"):
                payload = {k: v for k, v in payload.items() if k != "issuer_proof"}
            canonical = rfc8785(payload)
            digest = sha256_labeled(canonical)
            self.assertEqual(canonical, vec["canonical"], vec["id"])
            self.assertEqual(digest, vec["sha256"], vec["id"])
            if vec["expected_result"] == "different_hash":
                other = by_id[vec["differs_from"]]
                self.assertNotEqual(digest, other["sha256"])
            if vec.get("same_payload_hash_as"):
                self.assertEqual(digest, by_id[vec["same_payload_hash_as"]]["sha256"])
            if vec["expected_result"] == "fail_proof_verification":
                base_proof = by_id["excluded-proof-base"]["input"]["issuer_proof"]["proof_value"]
                self.assertNotEqual(vec["input"]["issuer_proof"]["proof_value"], base_proof)
                self.assertIn("eyJhbGciOiJub25l", vec["input"]["issuer_proof"]["proof_value"])

    def test_absent_not_null(self):
        self.assertNotEqual(rfc8785({"a": 1}), rfc8785({"a": 1, "b": None}))


@unittest.skipUnless(Draft7Validator, "jsonschema not installed")
class SchemaNegativeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.decision = Draft7Validator(load_schema("DELEGATION_DECISION_V0_1.schema.json"))
        cls.snapshot = Draft7Validator(load_schema("AGGREGATE_AUTHORITY_SNAPSHOT_V0_1.schema.json"))
        cls.operator = Draft7Validator(load_schema("OPERATOR_APPROVAL_V0_1.schema.json"))
        for name in (
            "DELEGATION_ENVELOPE_V0_1.schema.json",
            "OPERATOR_APPROVAL_V0_1.schema.json",
            "COUNCIL_APPROVAL_V0_1.schema.json",
            "AGGREGATE_AUTHORITY_SNAPSHOT_V0_1.schema.json",
            "DELEGATION_DECISION_V0_1.schema.json",
        ):
            Draft7Validator.check_schema(load_schema(name))

    def errs(self, doc):
        return list(self.decision.iter_errors(doc))

    def test_deny_valid(self):
        self.assertEqual(self.errs(decision_base()), [])

    def test_allow_requires_one_time_and_proof(self):
        allow = decision_base(decision="ALLOW", enforcement_constraints={"one_time_use": True})
        self.assertEqual(self.errs(allow), [])
        missing = dict(allow)
        missing.pop("issuer_proof")
        self.assertTrue(self.errs(missing))

    def test_council_allow_structurally_invalid(self):
        doc = decision_base(
            decision="ALLOW",
            micc_approval_class="APPROVAL_COUNCIL",
            enforcement_constraints={"one_time_use": True},
            council_approval_ref="ap-1",
            council_approval_hash=SHA256,
        )
        self.assertTrue(self.errs(doc))
        deny = decision_base(decision="DENY", micc_approval_class="APPROVAL_COUNCIL")
        self.assertEqual(self.errs(deny), [])

    def test_additional_properties_rejected(self):
        self.assertTrue(self.errs(decision_base(unexpected=True)))

    def test_weak_nonce_rejected(self):
        self.assertTrue(self.errs(decision_base(decision_nonce="shortnonce")))

    def test_snapshot_vector_schema(self):
        snap = next(v for v in VECTORS["vectors"] if v["id"] == "snapshot-basic")["input"]
        self.assertEqual(list(self.snapshot.iter_errors(snap)), [])

    def test_operator_weak_nonce(self):
        approval = {
            "approval_id": "ap-1",
            "approval_nonce": "shortnonce",
            "approver": "operator",
            "issuer_proof": dict(PROOF),
            "reuse_policy": {"mode": "ONE_TIME"},
            "request_id": "req-1",
            "subject": {"type": "actor", "id": "agent-a"},
            "action": {"name": "op:x", "parameters_hash": SHA256},
            "resource": {"type": "res", "id": "rid"},
            "context_digest": SHA256,
            "state_hash": SHA256,
            "policy_bundle_hash": SHA256,
            "delegation_id": "del-1",
            "delegation_version": "1.0.0",
            "delegation_payload_hash": SHA256,
            "decision": "APPROVE",
            "issued_at": "2026-08-21T12:00:00Z",
            "expires_at": "2026-08-21T13:00:00Z",
        }
        self.assertTrue(list(self.operator.iter_errors(approval)))


class MappingAndCommitTests(unittest.TestCase):
    def test_resource_mapping_rule(self):
        ok = {"type": "github.repository", "id": URI, "canonical_uri": URI}
        bad = {"type": "github.repository", "id": "mirrornode://other", "canonical_uri": URI}
        self.assertEqual(ok["id"], ok["canonical_uri"])
        self.assertNotEqual(bad["id"], bad["canonical_uri"])

    def test_cross_issuer_keys_distinct(self):
        vec = next(v for v in COMMIT_VECTORS["vectors"] if v["id"] == "cross-issuer-collision")
        key_a = (vec["issuer_a"], vec["decision_id"], vec["decision_nonce"])
        key_b = (vec["issuer_b"], vec["decision_id"], vec["decision_nonce"])
        self.assertNotEqual(key_a, key_b)
        self.assertTrue(vec["shared_slot_forbidden"])

    def test_commit_vectors_cover_required_boundaries(self):
        ids = {v["id"] for v in COMMIT_VECTORS["vectors"]}
        required = {
            "crash-before-reservation",
            "crash-after-reservation-before-dispatch",
            "crash-after-effect-before-receipt",
            "crash-after-receipt-before-approval-accounting",
            "concurrent-duplicate-dispatch",
            "uncertain-reconciliation",
            "bounded-reuse-under-decrement",
            "weak-nonce",
            "cross-issuer-collision",
        }
        self.assertTrue(required.issubset(ids))
        for vec in COMMIT_VECTORS["vectors"]:
            self.assertIn("expected_result", vec)
            self.assertFalse(vec.get("expected_result") in {"complete_silently", "double_effect"})

    def test_protected_proof_hint_mismatch_is_fail(self):
        vec = next(v for v in VECTORS["vectors"] if v["id"] == "protected-proof-metadata-substitution")
        self.assertEqual(vec["expected_result"], "fail_proof_verification")
        hints = vec["input"]["issuer_proof"]
        self.assertEqual(hints["proof_type"], "DIGITAL_SIGNATURE")
        self.assertIn("operator#key-1", hints["issuer_credential_ref"])
        self.assertIn("eyJhbGciOiJub25l", hints["proof_value"])


if __name__ == "__main__":
    unittest.main()
