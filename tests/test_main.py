from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_session():
    response = client.post("/sessions", json={"session_user": "  ABC  "})
    assert response.status_code == 200
    data = response.json()
    assert data["session_user"] == "abc"
    assert "created_at" in data
    assert "session_id" in data

def test_add_message():
    # Create a new session
    session_response = client.post("/sessions", json={"session_user": "user1"})
    session_id = session_response.json()["session_id"]

    # Add a message
    message = {"role": "user", "content": "Hello World"}
    response = client.post(f"/sessions/{session_id}/messages", json=message)
    assert response.status_code == 200
    assert response.json()["status"] == "Message added successfully"

def test_get_messages():
    # Create a new session
    session_response = client.post("/sessions", json={"session_user": "user2"})
    session_id = session_response.json()["session_id"]

    # Add messages
    client.post(f"/sessions/{session_id}/messages", json={"role": "user", "content": "Hi"})
    client.post(f"/sessions/{session_id}/messages", json={"role": "assistant", "content": "Hello"})

    # Get all messages
    response = client.get(f"/sessions/{session_id}/messages")
    assert response.status_code == 200
    assert len(response.json()) == 2

    # Filter by role
    response = client.get(f"/sessions/{session_id}/messages?role=user")
    assert response.status_code == 200
    assert all(msg["role"] == "user" for msg in response.json())