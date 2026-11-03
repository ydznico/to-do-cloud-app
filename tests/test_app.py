import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app import app


def setup_function():
    app.config["tasks"] = []


def test_home_page():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"My To-Do List" in response.data


def test_add_task():
    client = app.test_client()
    response = client.post("/add", data={"title": "Study Python"})

    assert response.status_code == 302
    assert len(app.config["tasks"]) == 1
    assert app.config["tasks"][0]["title"] == "Study Python"


def test_complete_task():
    app.config["tasks"] = [
        {"id": 1, "title": "Study Python", "completed": False}
    ]

    client = app.test_client()
    client.post("/toggle/1")

    assert app.config["tasks"][0]["completed"] is True


def test_delete_task():
    app.config["tasks"] = [
        {"id": 1, "title": "Study Python", "completed": False}
    ]

    client = app.test_client()
    client.post("/delete/1")

    assert len(app.config["tasks"]) == 0


def test_blank_task_is_not_added():
    client = app.test_client()
    client.post("/add", data={"title": "   "})

    assert app.config["tasks"] == []
