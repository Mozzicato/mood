from fastapi.testclient import TestClient
import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import backend.main as main

client = TestClient(main.app)


def test_debug_no_client(monkeypatch):
    # Ensure client None behavior
    monkeypatch.setattr(main, "client", None)
    monkeypatch.setenv("GROQ_API_KEY", "")
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)

    r = client.get("/debug")
    assert r.status_code == 200
    data = r.json()
    assert data["client_initialized"] is False
    assert data["has_groq_env"] is False


def test_debug_client_initialized(monkeypatch):
    # Simulate client existing and a failing test_call
    class FakeClient:
        class chat:
            @staticmethod
            def completions(*args, **kwargs):
                raise Exception("simulated failure")

    monkeypatch.setattr(main, "client", FakeClient)
    monkeypatch.setenv("GROQ_API_KEY", "fake")

    r = client.get("/debug")
    assert r.status_code == 200
    data = r.json()
    assert data["client_initialized"] is True
    assert data["has_groq_env"] is True

    r2 = client.get("/debug?do_call=true")
    assert r2.status_code == 200
    assert "test_call" in r2.json()
