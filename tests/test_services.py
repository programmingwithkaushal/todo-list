"""
Unit tests for services module.
"""
from app import services
from app.models import Todo

def test_create_todo():
    todo = services.create_todo("Test Title", "Test Desc")
    assert isinstance(todo, Todo)
    assert todo.title == "Test Title"
    assert todo.description == "Test Desc"
    assert todo.status == "pending"

def test_get_all_todos():
    services.create_todo("T1")
    services.create_todo("T2")
    todos = services.get_all_todos()
    assert len(todos) >= 2

def test_get_todo_by_id():
    todo = services.create_todo("T1")
    fetched = services.get_todo_by_id(todo.id)
    assert fetched is not None
    assert fetched.id == todo.id

def test_update_todo():
    todo = services.create_todo("T1", "Desc1")
    updated = services.update_todo(todo.id, "T2", "Desc2", "completed")
    assert updated is not None
    assert updated.title == "T2"
    assert updated.status == "completed"

def test_delete_todo():
    todo = services.create_todo("T1")
    success = services.delete_todo(todo.id)
    assert success is True
    assert services.get_todo_by_id(todo.id) is None

def test_complete_todo():
    todo = services.create_todo("T1")
    completed = services.complete_todo(todo.id)
    assert completed is not None
    assert completed.status == "completed"

def test_search_todos():
    services.create_todo("Apple")
    services.create_todo("Banana")
    results = services.search_todos("App")
    assert len(results) == 1
    assert results[0].title == "Apple"

def test_filter_completed():
    todo = services.create_todo("T1")
    services.complete_todo(todo.id)
    results = services.filter_completed()
    assert len(results) >= 1
    assert all(t.status == "completed" for t in results)

def test_filter_pending():
    services.create_todo("T1")
    results = services.filter_pending()
    assert len(results) >= 1
    assert all(t.status == "pending" for t in results)
