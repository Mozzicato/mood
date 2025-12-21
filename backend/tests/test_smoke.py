from fastapi.testclient import TestClient
import backend.main as main

client = TestClient(main.app)


def test_root():
    r = client.get("/")
    assert r.status_code == 200
    assert r.json() == {"message": "Welcome to TheraMood AI API"}


def test_crisis_detection():
    payload = {
        "message": "I might kill myself",
        "emotion": "Sad",
        "history": []
    }
    r = client.post("/chat", json=payload)
    assert r.status_code == 200
    assert "call emergency services" in r.json()["message"]


def test_fallback_on_api_error(monkeypatch):
    # Force the OpenAI client to raise an exception to trigger fallback
    class BrokenClient:
        class chat:
            @staticmethod
            def completions():
                raise Exception("simulated failure")

    # Monkeypatch the client in main
    monkeypatch.setattr(main, "client", BrokenClient)

    payload = {
        "message": "Hello",
        "emotion": "Happy",
        "history": []
    }
    r = client.post("/chat", json=payload)
    assert r.status_code == 200
    assert "(Offline)" in r.json()["message"]
