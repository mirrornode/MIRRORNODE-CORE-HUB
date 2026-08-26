from fastapi.testclient import TestClient

from hermes import runtime


client = TestClient(runtime.app)


def setup_function():
    runtime.message_queue.clear()


def test_route_reports_volatile_queue_not_delivery():
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

    assert response.status_code == 202
    body = response.json()
    assert body["accepted"] is True
    assert body["transport_state"] == "ACCEPTED"
    assert body["durable"] is False
    assert body["delivered"] is False
    assert "routed" not in body


def test_flush_queue_is_not_exposed():
    response = client.delete("/queue")
    assert response.status_code == 405
