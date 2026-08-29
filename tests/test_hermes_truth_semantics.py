from fastapi.testclient import TestClient

from hermes import runtime


client = TestClient(runtime.app)


def setup_function():
    runtime.message_queue.clear()


def test_route_reports_volatile_buffer_not_delivery(monkeypatch):
    audit_calls = []
    monkeypatch.setattr(runtime, "emit_audit", lambda **kwargs: audit_calls.append(kwargs) or "test-audit")

    response = client.post(
        "/route",
        json={
            "from_agent": "TEST_PRODUCER",
            "to_agent": "TEST_CONSUMER",
            "message_type": "test.event",
            "payload": {"hello": "world"},
            "priority": 5,
        },
    )

    assert response.status_code == 200
    body = response.json()
    assert body["buffered"] is True
    assert body["prototype_state"] == "VOLATILE_BUFFERED"
    assert body["transport_state"] is None
    assert body["durable"] is False
    assert body["delivered"] is False
    assert "routed" not in body
    assert "accepted" not in body

    assert len(audit_calls) == 1
    evidence = audit_calls[0]["evidence"]
    assert evidence["event"] == "message_buffered_volatile"
    assert evidence["transport_state"] is None
    assert evidence["durable"] is False
    assert evidence["delivered"] is False


def test_ingest_reports_volatile_buffer_not_transport_acceptance(monkeypatch):
    audit_calls = []
    monkeypatch.setattr(runtime, "emit_audit", lambda **kwargs: audit_calls.append(kwargs) or "test-audit")

    response = client.post(
        "/ingest",
        headers={"x-source": "test-source"},
        json={"event": "fixture"},
    )

    assert response.status_code == 200
    body = response.json()
    assert body["buffered"] is True
    assert body["prototype_state"] == "VOLATILE_BUFFERED"
    assert body["transport_state"] is None
    assert body["durable"] is False
    assert body["delivered"] is False

    assert len(audit_calls) == 1
    evidence = audit_calls[0]["evidence"]
    assert evidence["event"] == "webhook_buffered_volatile"
    assert evidence["transport_state"] is None


def test_flush_queue_is_not_exposed():
    response = client.delete("/queue")
    assert response.status_code == 405
