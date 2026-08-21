"""RFC 8785 JCS subset used by CG-0036 fixture tests.

Object names are ordered by UTF-16 code units (RFC 8785 §3.2.3), not
Unicode code points. Python json.dumps(sort_keys=True) is not used.
"""

from __future__ import annotations

import hashlib
import json
from typing import Any


SET_LIKE_ARRAYS = {
    "allowed_operations",
    "resource_scope",
    "environment_scope",
    "applicable_delegation_payload_hashes",
    "eligible_operations",
}

SEQUENCE_ARRAYS = {
    "obligations",
    "notes",
}

# IEEE-754 binary64 exact integers (RFC 8785 / I-JSON).
IJSON_INT_MAX = (2**53) - 1
IJSON_INT_MIN = -IJSON_INT_MAX


def require_ijson_int(value: int) -> None:
    if value < IJSON_INT_MIN or value > IJSON_INT_MAX:
        raise ValueError("non-ijson integer")


def utf16_code_units(s: str) -> bytes:
    return s.encode("utf-16-be")


def json_string(s: str) -> str:
    return json.dumps(s, ensure_ascii=False)


def jcs(value: Any) -> str:
    if value is None:
        return "null"
    if value is True:
        return "true"
    if value is False:
        return "false"
    if isinstance(value, str):
        return json_string(value)
    if isinstance(value, int) and not isinstance(value, bool):
        require_ijson_int(value)
        return str(value)
    if isinstance(value, float):
        raise ValueError("non-ijson float")
    if isinstance(value, list):
        return "[" + ",".join(jcs(item) for item in value) + "]"
    if isinstance(value, dict):
        keys = sorted(value.keys(), key=utf16_code_units)
        return "{" + ",".join(json_string(k) + ":" + jcs(value[k]) for k in keys) + "}"
    raise TypeError(f"unsupported JCS type: {type(value)!r}")


def sort_set_like_array(items: list) -> list:
    encoded = [jcs(item) for item in items]
    if len(encoded) != len(set(encoded)):
        raise ValueError("duplicate set-like array item")
    order = sorted(range(len(items)), key=lambda i: encoded[i].encode("utf-8"))
    return [items[i] for i in order]


def preprocess_set_like(value: Any, key: str | None = None) -> Any:
    if isinstance(value, list):
        if key in SET_LIKE_ARRAYS:
            prepared = [preprocess_set_like(item, None) for item in value]
            return sort_set_like_array(prepared)
        if key in SEQUENCE_ARRAYS or key is None:
            return [preprocess_set_like(item, None) for item in value]
        return [preprocess_set_like(item, None) for item in value]
    if isinstance(value, dict):
        return {k: preprocess_set_like(v, k) for k, v in value.items()}
    return value


def payload_excluding_issuer_proof(obj: dict) -> dict:
    return {k: v for k, v in obj.items() if k != "issuer_proof"}


def child_issuer_bound_to_parent_delegate(parent: dict, child: dict, *, live_identity_registry_hash: str | None) -> bool:
    """True iff the child's authenticated logical issuer is the parent delegate identity."""
    if child.get("issuer_authority_kind") != "PARENT_ENVELOPE":
        return False
    parent_delegate = parent.get("delegate_logical_issuer_id")
    child_issuer = child.get("logical_issuer_id")
    if not parent_delegate or not child_issuer:
        return False
    if child_issuer != parent_delegate:
        return False
    bound_hash = parent.get("delegate_identity_registry_snapshot_hash")
    if not bound_hash or not live_identity_registry_hash:
        return False
    if bound_hash != live_identity_registry_hash:
        return False
    return True


def canonical_hash(obj: dict, *, exclude_issuer_proof: bool = False) -> tuple[str, str]:
    prepared = dict(obj)
    if exclude_issuer_proof:
        prepared = payload_excluding_issuer_proof(prepared)
    prepared = preprocess_set_like(prepared)
    canonical = jcs(prepared)
    digest = "sha256:" + hashlib.sha256(canonical.encode("utf-8")).hexdigest()
    return canonical, digest
