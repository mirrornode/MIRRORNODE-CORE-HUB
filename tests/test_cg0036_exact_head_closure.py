#!/usr/bin/env python3
"""Exact-head closure tests for the bounded CG-0036 Codex findings."""

from __future__ import annotations

import json
from pathlib import Path

from jsonschema import Draft7Validator


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
    validator = Draft7Validator(load_schema("DECISION_PRECONDITIONS_V0_1.schema.json"))
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
