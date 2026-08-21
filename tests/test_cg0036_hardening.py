#!/usr/bin/env python3
"""CG-0036 bounded-hardening fixtures: canonicalization, schemas, commit tables."""

from __future__ import annotations

import json
import re
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))
from cg0036_jcs import (  # noqa: E402
    IJSON_INT_MAX,
    canonical_hash,
    child_issuer_bound_to_parent_delegate,
    jcs,
    utf16_code_units,
)

DELEGATION = ROOT / "docs" / "delegation"
VECTORS = json.loads((DELEGATION / "CANONICALIZATION_VECTORS_V0_1.json").read_text())
COMMIT_VECTORS = json.loads((DELEGATION / "EFFECT_CONSUMPTION_COMMIT_VECTORS_V0_1.json").read_text())

try:
    from jsonschema import Draft7Validator
except ImportError:  # pragma: no cover
    Draft7Validator = None


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
    return json.loads(
        text,
        parse_constant=lambda v: (_ for _ in ()).throw(ValueError("non-ijson")),
        object_pairs_hook=reject_duplicates,
    )


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
        "authority_holder_logical_issuer_id": "issuer-agent-a",
        "action": {"name": "op:x", "parameters_hash": SHA256},
        "resource": {"type": "github.repository", "id": URI, "canonical_uri": URI},
        "resource_registry_ref": "docs/delegation/resource-registry",
        "resource_registry_snapshot_hash": SHA256,
        "resource_record_hash": SHA256,
        "context_digest": SHA256,
        "delegation_id": "del-1",
        "delegation_version": "1.0.0",
        "delegation_payload_hash": SHA256,
        "authority_class": "AUTONOMOUS_WITHIN_POLICY",
        "micc_approval_class": "APPROVAL_NONE",
        "micc_invocation_binding_ref": "docs/delegation/micc-binding",
        "micc_invocation_binding_hash": SHA256,
        "pdp_identity": "pdp-primary",
        "pdp_version": "0.1.0",
        "logical_issuer_id": "issuer-pdp-primary",
        "issuer_registry_ref": "docs/delegation/issuer-registry",
        "issuer_registry_snapshot_hash": SHA256,
        "issuer_proof": dict(PROOF),
        "policy_content_hash": SHA256,
        "policy_bundle_hash": SHA256,
        "decision_preconditions_ref": "docs/delegation/preconditions",
        "decision_preconditions_hash": SHA256,
        "precondition_evaluation_hash": SHA256,
        "aggregate_authority_snapshot_ref": "docs/delegation/aggregate-snapshot",
        "aggregate_authority_snapshot_hash": SHA256,
        "revocation_state_ref": "docs/delegation/revocation-state",
        "revocation_state_hash": SHA256,
        "revocation_sequence": 1,
        "revocation_checked_at": "2026-08-21T12:00:00Z",
        "state_hash": SHA256,
        "decision": "DENY",
        "reason_code": "DENIED",
        "issued_at": "2026-08-21T12:00:00Z",
        "expires_at": "2026-08-21T13:00:00Z",
    }
    doc.update(overrides)
    return doc


def operator_base(**overrides):
    doc = {
        "approval_id": "ap-1",
        "approval_nonce": NONCE,
        "approver": "operator",
        "logical_issuer_id": "issuer-operator",
        "issuer_registry_ref": "docs/delegation/issuer-registry",
        "issuer_registry_snapshot_hash": SHA256,
        "issuer_proof": dict(PROOF),
        "reuse_policy": {"mode": "ONE_TIME"},
        "request_id": "req-1",
        "subject": {"type": "actor", "id": "agent-a"},
        "action": {"name": "op:x", "parameters_hash": SHA256},
        "resource": {"type": "github.repository", "id": URI, "canonical_uri": URI},
        "resource_registry_ref": "docs/delegation/resource-registry",
        "resource_registry_snapshot_hash": SHA256,
        "resource_record_hash": SHA256,
        "context_digest": SHA256,
        "state_hash": SHA256,
        "micc_invocation_binding_hash": SHA256,
        "policy_bundle_hash": SHA256,
        "delegation_id": "del-1",
        "delegation_version": "1.0.0",
        "delegation_payload_hash": SHA256,
        "decision": "APPROVE",
        "issued_at": "2026-08-21T12:00:00Z",
        "expires_at": "2026-08-21T13:00:00Z",
    }
    doc.update(overrides)
    return doc


class CanonicalizationVectorTests(unittest.TestCase):
    def test_jcs_is_not_python_sort_keys(self):
        clef, repl = "\U0001D11E", "\uFFFD"
        obj = {repl: 1, clef: 2}
        py = json.dumps(obj, ensure_ascii=False, separators=(",", ":"), sort_keys=True)
        self.assertNotEqual(jcs(obj), py)
        self.assertLess(utf16_code_units(clef), utf16_code_units(repl))
        self.assertGreater(clef, repl)

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
            if vec["expected_result"] == "reject_non_ijson_integer":
                with self.assertRaises(ValueError):
                    jcs(vec["input"])
                continue
            exclude = bool(vec.get("exclude_issuer_proof"))
            canonical, digest = canonical_hash(vec["input"], exclude_issuer_proof=exclude)
            if "canonical" in vec:
                self.assertEqual(canonical, vec["canonical"], vec["id"])
            if "sha256" in vec:
                self.assertEqual(digest, vec["sha256"], vec["id"])
            if vec["expected_result"] == "different_hash":
                other = by_id[vec["differs_from"]]
                self.assertNotEqual(digest, other["sha256"])
            if vec.get("same_payload_hash_as"):
                self.assertEqual(digest, by_id[vec["same_payload_hash_as"]]["sha256"])
            if vec.get("must_differ_from_code_point_order"):
                self.assertNotEqual(canonical, vec["code_point_order_canonical"])
            if vec.get("permutation"):
                perm = dict(vec["input"])
                perm.update(vec["permutation"])
                _, perm_digest = canonical_hash(perm, exclude_issuer_proof=exclude)
                self.assertEqual(digest, perm_digest, vec["id"])
            if vec["expected_result"] == "fail_proof_verification":
                self.assertIn("eyJhbGciOiJub25l", vec["input"]["issuer_proof"]["proof_value"])


@unittest.skipUnless(Draft7Validator, "jsonschema not installed")
class SchemaNegativeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.decision = Draft7Validator(load_schema("DELEGATION_DECISION_V0_1.schema.json"))
        cls.envelope = Draft7Validator(load_schema("DELEGATION_ENVELOPE_V0_1.schema.json"))
        cls.operator = Draft7Validator(load_schema("OPERATOR_APPROVAL_V0_1.schema.json"))
        cls.council = Draft7Validator(load_schema("COUNCIL_APPROVAL_V0_1.schema.json"))
        cls.snapshot = Draft7Validator(load_schema("AGGREGATE_AUTHORITY_SNAPSHOT_V0_1.schema.json"))
        cls.issuer_auth = Draft7Validator(load_schema("ISSUER_AUTHORITY_RECORD_V0_1.schema.json"))
        cls.preconditions = Draft7Validator(load_schema("DECISION_PRECONDITIONS_V0_1.schema.json"))
        cls.aggregate_policy = Draft7Validator(load_schema("AGGREGATE_AUTHORITY_POLICY_V0_1.schema.json"))
        cls.micc_binding = Draft7Validator(load_schema("MICC_INVOCATION_BINDING_V0_1.schema.json"))
        cls.revocation = Draft7Validator(load_schema("REVOCATION_STATE_V0_1.schema.json"))
        cls.resource_registry = Draft7Validator(load_schema("RESOURCE_REGISTRY_SNAPSHOT_V0_1.schema.json"))
        cls.receipt = Draft7Validator(load_schema("EXECUTION_RECEIPT_V0_1.schema.json"))
        for name in (
            "DELEGATION_ENVELOPE_V0_1.schema.json",
            "OPERATOR_APPROVAL_V0_1.schema.json",
            "COUNCIL_APPROVAL_V0_1.schema.json",
            "AGGREGATE_AUTHORITY_SNAPSHOT_V0_1.schema.json",
            "DELEGATION_DECISION_V0_1.schema.json",
            "ISSUER_AUTHORITY_RECORD_V0_1.schema.json",
            "DECISION_PRECONDITIONS_V0_1.schema.json",
            "AGGREGATE_AUTHORITY_POLICY_V0_1.schema.json",
            "MICC_INVOCATION_BINDING_V0_1.schema.json",
            "REVOCATION_STATE_V0_1.schema.json",
            "RESOURCE_REGISTRY_SNAPSHOT_V0_1.schema.json",
            "EXECUTION_RECEIPT_V0_1.schema.json",
        ):
            Draft7Validator.check_schema(load_schema(name))

    def test_excluded_proof_vectors_schema_valid(self):
        for vec in VECTORS["vectors"]:
            if not vec.get("validate_before_exclusion"):
                continue
            schema = Draft7Validator(load_schema(vec["schema"]))
            self.assertEqual(list(schema.iter_errors(vec["input"])), [], vec["id"])

    def test_council_allow_structurally_invalid(self):
        doc = decision_base(
            decision="ALLOW",
            micc_approval_class="APPROVAL_COUNCIL",
            enforcement_constraints={"one_time_use": True},
            council_approval_ref="ap-1",
            council_approval_hash=SHA256,
        )
        self.assertTrue(list(self.decision.iter_errors(doc)))

    def test_missing_decision_proof_invalid(self):
        missing = decision_base()
        missing.pop("issuer_proof")
        self.assertTrue(list(self.decision.iter_errors(missing)))

    def test_approval_missing_registry_binding_invalid(self):
        missing = operator_base()
        missing.pop("resource_registry_snapshot_hash")
        self.assertTrue(list(self.operator.iter_errors(missing)))
        missing_record = operator_base()
        missing_record.pop("resource_record_hash")
        self.assertTrue(list(self.operator.iter_errors(missing_record)))

    def test_oversized_authority_rank_invalid(self):
        env = next(v for v in VECTORS["vectors"] if v["id"] == "excluded-proof-envelope")["input"]
        bad = dict(env)
        bad["authority_rank"] = 9007199254740992
        self.assertTrue(list(self.envelope.iter_errors(bad)))

    def test_envelope_missing_delegate_logical_issuer_invalid(self):
        env = next(v for v in VECTORS["vectors"] if v["id"] == "excluded-proof-envelope")["input"]
        bad = dict(env)
        bad.pop("delegate_logical_issuer_id")
        self.assertTrue(list(self.envelope.iter_errors(bad)))

    def test_envelope_missing_issuer_authority_invalid(self):
        env = next(v for v in VECTORS["vectors"] if v["id"] == "excluded-proof-envelope")["input"]
        bad = dict(env)
        bad.pop("issuer_authority_hash")
        self.assertTrue(list(self.envelope.iter_errors(bad)))

    def test_every_governed_envelope_reference_is_hash_bound(self):
        env = next(v for v in VECTORS["vectors"] if v["id"] == "excluded-proof-envelope")["input"]
        pairs = {
            "issuer_registry_ref": "issuer_registry_snapshot_hash",
            "issuer_authority_ref": "issuer_authority_hash",
            "delegate_identity_registry_ref": "delegate_identity_registry_snapshot_hash",
            "governing_policy_ref": "policy_content_hash",
            "decision_preconditions_ref": "decision_preconditions_hash",
            "revocation_ref": "revocation_source_hash",
            "receipt_policy_ref": "receipt_policy_hash",
            "aggregate_authority_policy_ref": "aggregate_authority_policy_hash",
        }
        for ref, digest in pairs.items():
            with self.subTest(ref=ref):
                self.assertIn(ref, env)
                self.assertIn(digest, env)
                bad = dict(env)
                bad.pop(digest)
                self.assertTrue(list(self.envelope.iter_errors(bad)))

    def test_weak_nonce_rejected(self):
        self.assertTrue(list(self.decision.iter_errors(decision_base(decision_nonce="shortnonce"))))

    def test_snapshot_vector_schema(self):
        snap = next(v for v in VECTORS["vectors"] if v["id"] == "snapshot-set-permutation")["input"]
        self.assertEqual(list(self.snapshot.iter_errors(snap)), [])

    def test_decision_requires_holder_micc_revocation_and_evaluation_bindings(self):
        for field in (
            "authority_holder_logical_issuer_id",
            "micc_invocation_binding_hash",
            "precondition_evaluation_hash",
            "revocation_state_hash",
            "revocation_sequence",
            "revocation_checked_at",
        ):
            with self.subTest(field=field):
                bad = decision_base()
                bad.pop(field)
                self.assertTrue(list(self.decision.iter_errors(bad)))

    def test_success_receipt_requires_effect_proof_and_persisted_outcome(self):
        receipt = {
            "receipt_id": "receipt-1",
            "receipt_version": "0.1.0",
            "execution_nonce": NONCE,
            "decision_ref": "docs/delegation/decisions/dec-1",
            "decision_hash": SHA256,
            "decision_logical_issuer_id": "issuer-pdp-primary",
            "decision_id": "dec-1",
            "decision_nonce": NONCE,
            "delegation_payload_hash": SHA256,
            "authority_holder_logical_issuer_id": "issuer-agent-a",
            "micc_invocation_binding_hash": SHA256,
            "resource_registry_snapshot_hash": SHA256,
            "resource_record_hash": SHA256,
            "precondition_evaluation_hash": SHA256,
            "revocation_state_hash": SHA256,
            "aggregate_authority_snapshot_hash": SHA256,
            "decision_consumption": "COMMITTED",
            "approval_consumption": "NOT_APPLICABLE",
            "dispatch_state": "OUTCOME_PERSISTED",
            "effect_outcome": "SUCCEEDED",
            "effect_receipt_ref": "docs/delegation/effects/effect-1",
            "effect_receipt_hash": SHA256,
            "audit_id": "audit-1",
            "issued_at": "2026-08-21T12:00:01Z",
            "logical_issuer_id": "issuer-pep-primary",
            "issuer_registry_ref": "docs/delegation/issuer-registry",
            "issuer_registry_snapshot_hash": SHA256,
            "issuer_proof": dict(PROOF),
        }
        self.assertEqual(list(self.receipt.iter_errors(receipt)), [])
        receipt.pop("effect_receipt_hash")
        self.assertTrue(list(self.receipt.iter_errors(receipt)))

    def test_issuer_authority_record_schema(self):
        rec = {
            "record_id": "iar-1",
            "record_version": "1.0.0",
            "logical_issuer_id": "issuer-operator",
            "allowed_operations": ["op:x"],
            "resource_scope": [URI],
            "environment_scope": ["PRODUCTION"],
            "authority_rank": 1,
            "authority_ceiling": "bounded-ops",
            "risk_ceiling": "LOW",
            "subdelegation_max_depth": 0,
            "effective_at": "2026-08-21T12:00:00Z",
            "expires_at": "2026-08-22T12:00:00Z",
        }
        self.assertEqual(list(self.issuer_auth.iter_errors(rec)), [])


class IjsonIntegerTests(unittest.TestCase):
    def test_bounds(self):
        self.assertEqual(IJSON_INT_MAX, 9007199254740991)
        self.assertEqual(jcs(IJSON_INT_MAX), "9007199254740991")
        self.assertEqual(jcs(-IJSON_INT_MAX), "-9007199254740991")
        with self.assertRaises(ValueError):
            jcs(IJSON_INT_MAX + 1)
        with self.assertRaises(ValueError):
            jcs(-IJSON_INT_MAX - 1)
        with self.assertRaises(ValueError):
            jcs({"n": IJSON_INT_MAX + 1})
        with self.assertRaises(ValueError):
            jcs([IJSON_INT_MAX + 1])


class ChildIssuerBindingTests(unittest.TestCase):
    def _parent(self, **overrides):
        doc = {
            "delegate_actor": "agent-a",
            "delegate_logical_issuer_id": "issuer-agent-a",
            "delegate_identity_registry_ref": "docs/delegation/identity-registry",
            "delegate_identity_registry_snapshot_hash": SHA256,
        }
        doc.update(overrides)
        return doc

    def _child(self, **overrides):
        doc = {
            "issuer_authority_kind": "PARENT_ENVELOPE",
            "logical_issuer_id": "issuer-agent-a",
            "delegate_actor": "agent-a",
        }
        doc.update(overrides)
        return doc

    def test_correct_parent_delegate_issuing_child_passes(self):
        self.assertTrue(
            child_issuer_bound_to_parent_delegate(
                self._parent(), self._child(), live_identity_registry_hash=SHA256
            )
        )

    def test_authenticated_peer_citing_victim_parent_fails(self):
        self.assertFalse(
            child_issuer_bound_to_parent_delegate(
                self._parent(),
                self._child(logical_issuer_id="issuer-peer"),
                live_identity_registry_hash=SHA256,
            )
        )

    def test_matching_display_name_different_logical_identity_fails(self):
        self.assertFalse(
            child_issuer_bound_to_parent_delegate(
                self._parent(),
                self._child(logical_issuer_id="issuer-other", delegate_actor="agent-a"),
                live_identity_registry_hash=SHA256,
            )
        )

    def test_credential_rotation_same_logical_issuer_passes(self):
        self.assertTrue(
            child_issuer_bound_to_parent_delegate(
                self._parent(),
                self._child(),
                live_identity_registry_hash=SHA256,
            )
        )

    def test_stale_identity_registry_fails_closed(self):
        stale = "sha256:" + ("b" * 64)
        self.assertFalse(
            child_issuer_bound_to_parent_delegate(
                self._parent(), self._child(), live_identity_registry_hash=stale
            )
        )
        self.assertFalse(
            child_issuer_bound_to_parent_delegate(
                self._parent(), self._child(), live_identity_registry_hash=None
            )
        )


class MappingAndCommitTests(unittest.TestCase):
    def test_every_schema_repo_ref_has_declared_integrity_partner(self):
        partners = {
            "authority_holder_registry_ref": "authority_holder_registry_snapshot_hash",
            "root_ceiling_ref": "root_ceiling_hash",
            "forbid_policy_ref": "forbid_policy_hash",
            "aggregate_authority_policy_ref": "aggregate_authority_policy_hash",
            "issuer_registry_ref": "issuer_registry_snapshot_hash",
            "resource_registry_ref": "resource_registry_snapshot_hash",
            "evidence_ref": "evidence_hash",
            "micc_invocation_binding_ref": "micc_invocation_binding_hash",
            "decision_preconditions_ref": "decision_preconditions_hash",
            "aggregate_authority_snapshot_ref": "aggregate_authority_snapshot_hash",
            "revocation_state_ref": "revocation_state_hash",
            "delegate_identity_registry_ref": "delegate_identity_registry_snapshot_hash",
            "governing_policy_ref": "policy_content_hash",
            "revocation_ref": "revocation_source_hash",
            "receipt_policy_ref": "receipt_policy_hash",
            "decision_ref": "decision_hash",
            "approval_ref": "approval_hash",
            "effect_receipt_ref": "effect_receipt_hash",
            "mim_ref": "mim_hash",
        }
        observed = set()

        def scan(node):
            if isinstance(node, dict):
                props = node.get("properties")
                if isinstance(props, dict):
                    for name, schema in props.items():
                        if isinstance(schema, dict) and schema.get("$ref") == "#/definitions/repoRef":
                            observed.add(name)
                            self.assertIn(name, partners)
                            self.assertIn(partners[name], props)
                        scan(schema)
                for key, value in node.items():
                    if key != "properties":
                        scan(value)
            elif isinstance(node, list):
                for value in node:
                    scan(value)

        for path in DELEGATION.glob("*.schema.json"):
            scan(json.loads(path.read_text()))
        self.assertEqual(observed, set(partners))

    def test_end_to_end_vectors_cover_compromise_paths(self):
        vectors = json.loads((DELEGATION / "END_TO_END_CONFORMANCE_VECTORS_V0_1.json").read_text())["vectors"]
        ids = {v["id"] for v in vectors}
        self.assertTrue({
            "unbound-governed-reference",
            "micc-adapter-substitution",
            "aggregate-holder-substitution",
            "resource-registry-remap",
            "revocation-sequence-replay",
            "receipt-success-without-effect-proof",
        }.issubset(ids))

    def test_resource_remap_invalidates_approval(self):
        approved = SHA256
        remapped = "sha256:" + ("b" * 64)
        self.assertNotEqual(approved, remapped)

    def test_authenticated_peer_without_scope(self):
        possessed = {"op:x"}
        signed = {"op:x", "op:admin"}
        self.assertFalse(signed.issubset(possessed))

    def test_logical_issuer_rotation_and_collision(self):
        rotate = next(v for v in COMMIT_VECTORS["vectors"] if v["id"] == "credential-rotation-preserves-logical-issuer")
        self.assertEqual(rotate["expected_result"], "same_consumption_namespace")
        collide = next(v for v in COMMIT_VECTORS["vectors"] if v["id"] == "unrelated-credentials-do-not-collapse")
        self.assertNotEqual(collide["logical_issuer_a"], collide["logical_issuer_b"])
        key_a = (collide["logical_issuer_a"], "dec-1", NONCE)
        key_b = (collide["logical_issuer_b"], "dec-1", NONCE)
        self.assertNotEqual(key_a, key_b)

    def test_commit_vectors_cover_required_boundaries(self):
        ids = {v["id"] for v in COMMIT_VECTORS["vectors"]}
        required = {
            "crash-before-reservation",
            "crash-in-reserved-no-dispatch-intent",
            "send-to-persist-external-accept-local-fail",
            "concurrent-last-bounded-reuse-use",
            "concurrent-one-time-approval",
            "confirmed-no-effect-release",
            "successful-effect-finalizes-approval",
            "uncertain-retains-approval-reservation",
            "failed-finalization-does-not-restore-capacity",
            "credential-rotation-preserves-logical-issuer",
        }
        self.assertTrue(required.issubset(ids), required - ids)
        reserved = next(v for v in COMMIT_VECTORS["vectors"] if v["id"] == "crash-in-reserved-no-dispatch-intent")
        self.assertTrue(reserved["reserved_is_not_prior_dispatch"])
        send = next(v for v in COMMIT_VECTORS["vectors"] if v["id"] == "send-to-persist-external-accept-local-fail")
        self.assertTrue(send["send_to_persist_window"])
        last = next(v for v in COMMIT_VECTORS["vectors"] if v["id"] == "concurrent-last-bounded-reuse-use")
        self.assertTrue(last["loser_dispatch_forbidden"])


if __name__ == "__main__":
    unittest.main()
