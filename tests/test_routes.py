"""
Unit tests for API routes.
"""
import json

def test_get_todos_empty(client):
    response = client.get("/todos")
    assert response.status_code == 200
    assert response.json["data"] == []

def test_create_todo_route(client):
    response = client.post(
        "/todos",
        data=json.dumps({"title": "Buy Milk"}),
        content_type="application/json",
    )
    assert response.status_code == 201
    assert response.json["data"]["title"] == "Buy Milk"

def test_create_todo_invalid(client):
    response = client.post(
        "/todos",
        data=json.dumps({"description": "No title"}),
        content_type="application/json",
    )
    assert response.status_code == 400

def test_get_todo_route(client):
    create_res = client.post(
        "/todos",
        data=json.dumps({"title": "Test"}),
        content_type="application/json",
    )
    todo_id = create_res.json["data"]["id"]

    response = client.get(f"/todos/{todo_id}")
    assert response.status_code == 200
    assert response.json["data"]["title"] == "Test"

def test_update_todo_route(client):
    create_res = client.post(
        "/todos",
        data=json.dumps({"title": "Test"}),
        content_type="application/json",
    )
    todo_id = create_res.json["data"]["id"]

    response = client.put(
        f"/todos/{todo_id}",
        data=json.dumps({"title": "Updated", "status": "completed"}),
        content_type="application/json",
    )
    assert response.status_code == 200
    assert response.json["data"]["title"] == "Updated"
    assert response.json["data"]["status"] == "completed"

def test_delete_todo_route(client):
    create_res = client.post(
        "/todos",
        data=json.dumps({"title": "Test"}),
        content_type="application/json",
    )
    todo_id = create_res.json["data"]["id"]

    response = client.delete(f"/todos/{todo_id}")
    assert response.status_code == 200

    get_res = client.get(f"/todos/{todo_id}")
    assert get_res.status_code == 404

def test_complete_todo_route(client):
    create_res = client.post(
        "/todos",
        data=json.dumps({"title": "Test"}),
        content_type="application/json",
    )
    todo_id = create_res.json["data"]["id"]

    response = client.patch(f"/todos/{todo_id}/complete")
    assert response.status_code == 200
    assert response.json["data"]["status"] == "completed"

def test_search_todos_route(client):
    client.post(
        "/todos",
        data=json.dumps({"title": "Find Me"}),
        content_type="application/json",
    )
    response = client.get("/todos/search?q=Find")
    assert response.status_code == 200
    assert len(response.json["data"]) == 1

def test_filter_completed_route(client):
    create_res = client.post(
        "/todos",
        data=json.dumps({"title": "Test"}),
        content_type="application/json",
    )
    todo_id = create_res.json["data"]["id"]
    client.patch(f"/todos/{todo_id}/complete")

    response = client.get("/todos/completed")
    assert response.status_code == 200
    assert len(response.json["data"]) >= 1

def test_filter_pending_route(client):
    client.post(
        "/todos",
        data=json.dumps({"title": "Test"}),
        content_type="application/json",
    )
    response = client.get("/todos/pending")
    assert response.status_code == 200
    assert len(response.json["data"]) >= 1
