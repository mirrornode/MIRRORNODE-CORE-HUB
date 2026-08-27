#!/usr/bin/env python3
"""Exact-head closure tests for the bounded CG-0036 Codex findings."""

from __future__ import annotations

import json
from pathlib import Path

from jsonschema import Draft7Validator, FormatChecker


ROOT = Path(__file__).resolve().parents[1]
DELEGATION = ROOT / "docs" / "delegation"


def load_schema(name: str):
    return json.loads((DELEGATION / name).read_text())


def check(kind: str, operator: str, expected):
    return {
        "preconditions_id": "preconditions-closure",
        "preconditions_version": "0.1.0",
        "combiner": "ALL_MUST_PASS",
        "checks": [
            {
                "check_id": "check-closure",
                "kind": kind,
                "operator": operator,
                "target": "idempotency/closure",
                "expected": expected,
            }
        ],
    }


def errors(doc):
    validator = Draft7Validator(
        load_schema("DECISION_PRECONDITIONS_V0_1.schema.json"),
        format_checker=FormatChecker(),
    )
    return list(validator.iter_errors(doc))


def test_idempotency_equals_requires_nonempty_string_key():
    assert not errors(check("IDEMPOTENCY_KEY", "EQUALS", "request-key-1"))
    assert errors(check("IDEMPOTENCY_KEY", "EQUALS", 1))
    assert errors(check("IDEMPOTENCY_KEY", "EQUALS", True))
    assert errors(check("IDEMPOTENCY_KEY", "EQUALS", ""))


def test_idempotency_unseen_requires_literal_true():
    assert not errors(check("IDEMPOTENCY_KEY", "UNSEEN", True))
    assert errors(check("IDEMPOTENCY_KEY", "UNSEEN", False))
    assert errors(check("IDEMPOTENCY_KEY", "UNSEEN", "request-key-1"))
    assert errors(check("IDEMPOTENCY_KEY", "UNSEEN", 1))


def test_idempotency_rejects_unsupported_operators():
    assert errors(check("IDEMPOTENCY_KEY", "NOT_EQUALS", "request-key-1"))
    assert errors(check("IDEMPOTENCY_KEY", "AT_LEAST", "request-key-1"))
    assert errors(check("IDEMPOTENCY_KEY", "AT_MOST", "request-key-1"))


def test_aggregate_resource_scope_defers_to_single_jcs_set_ordering_rule():
    schema = load_schema("AGGREGATE_AUTHORITY_SNAPSHOT_V0_1.schema.json")
    description = schema["properties"]["resource_scope"]["description"]
    assert "RFC 8785 canonical representation" in description
    assert "Raw string-byte ordering is not a separate rule" in description

    profile = (DELEGATION / "AUTHORIZATION_EVALUATION_PROFILE_V0_1.md").read_text()
    assert "sort this set-like array only by the UTF-8 bytes of each item's RFC 8785 canonical representation" in profile
    assert "sorted ascending UTF-8 byte sequence of the request-relevant intersection" not in profile


def test_root_authority_requires_independent_governance_attestation_before_use():
    schema = load_schema("ISSUER_AUTHORITY_RECORD_V0_1.schema.json")
    attestation = schema["properties"]["governance_attestation"]
    assert {
        "governance_authority_logical_issuer_id",
        "governance_registry_ref",
        "governance_registry_snapshot_hash",
        "issuer_proof",
    }.issubset(set(attestation["required"]))

    profile = (DELEGATION / "AUTHORIZATION_EVALUATION_PROFILE_V0_1.md").read_text()
    assert "MUST contain `governance_attestation`" in profile
    assert "outside both the grant issuer's and grantee's authority path" in profile
    assert "self-issued" in profile


def test_authority_ceiling_is_exact_inheritance_token_in_v0_1():
    envelope = load_schema("DELEGATION_ENVELOPE_V0_1.schema.json")
    record = load_schema("ISSUER_AUTHORITY_RECORD_V0_1.schema.json")
    envelope_desc = envelope["properties"]["authority_ceiling"]["description"]
    record_desc = record["properties"]["authority_ceiling"]["description"]
    assert "ROOT_RECORD envelopes MUST exactly equal" in envelope_desc
    assert "PARENT_ENVELOPE children MUST exactly equal" in envelope_desc
    assert "defines no ordering" in envelope_desc
    assert "must inherit this exact token" in record_desc


def test_date_time_format_checker_rejects_calendar_invalid_timestamp():
    schema = load_schema("ISSUER_AUTHORITY_RECORD_V0_1.schema.json")
    validator = Draft7Validator(schema, format_checker=FormatChecker())
    record = {
        "record_id": "iar-closure",
        "record_version": "1.0.0",
        "logical_issuer_id": "issuer-operator",
        "allowed_operations": ["op:x"],
        "resource_scope": ["mirrornode://github/repository/MIRRORNODE-CORE-HUB"],
        "environment_scope": ["PRODUCTION"],
        "authority_rank": 1,
        "authority_ceiling": "bounded-ops",
        "risk_ceiling": "LOW",
        "budget_unit": "credits",
        "budget_ceiling": 10,
        "subdelegation_max_depth": 0,
        "effective_at": "2026-99-99T12:00:00Z",
        "expires_at": "2026-08-28T12:00:00Z",
    }
    assert list(validator.iter_errors(record))
