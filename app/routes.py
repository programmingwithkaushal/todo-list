"""
API Routing for Todos.
"""
from flask import Blueprint, request
from . import services
from .utils import create_response

todo_bp = Blueprint("todos", __name__, url_prefix="/todos")

@todo_bp.route("", methods=["GET"])
def get_todos():
    """Get all todos."""
    todos = services.get_all_todos()
    return create_response(data=[t.to_dict() for t in todos])

@todo_bp.route("/<int:todo_id>", methods=["GET"])
def get_todo(todo_id: int):
    """Get a specific todo by ID."""
    todo = services.get_todo_by_id(todo_id)
    if not todo:
        return create_response(error="Todo not found", status_code=404)
    return create_response(data=todo.to_dict())

@todo_bp.route("", methods=["POST"])
def create_todo():
    """Create a new todo."""
    data = request.get_json()
    if not data or "title" not in data:
        return create_response(error="Title is required", status_code=400)

    title = data["title"]
    description = data.get("description")
    todo = services.create_todo(title, description)
    return create_response(data=todo.to_dict(), status_code=201)

@todo_bp.route("/<int:todo_id>", methods=["PUT"])
def update_todo(todo_id: int):
    """Update an existing todo."""
    data = request.get_json()
    if not data or "title" not in data or "status" not in data:
        return create_response(error="Title and status are required", status_code=400)

    title = data["title"]
    description = data.get("description")
    status = data["status"]

    todo = services.update_todo(todo_id, title, description, status)
    if not todo:
        return create_response(error="Todo not found", status_code=404)

    return create_response(data=todo.to_dict())

@todo_bp.route("/<int:todo_id>", methods=["DELETE"])
def delete_todo(todo_id: int):
    """Delete a todo."""
    success = services.delete_todo(todo_id)
    if not success:
        return create_response(error="Todo not found", status_code=404)
    return create_response(data={"message": "Todo deleted successfully"})

@todo_bp.route("/<int:todo_id>/complete", methods=["PATCH"])
def complete_todo(todo_id: int):
    """Mark a todo as completed."""
    todo = services.complete_todo(todo_id)
    if not todo:
        return create_response(error="Todo not found", status_code=404)
    return create_response(data=todo.to_dict())

@todo_bp.route("/search", methods=["GET"])
def search_todos():
    """Search for todos."""
    query = request.args.get("q", "")
    todos = services.search_todos(query)
    return create_response(data=[t.to_dict() for t in todos])

@todo_bp.route("/completed", methods=["GET"])
def get_completed_todos():
    """Get all completed todos."""
    todos = services.filter_completed()
    return create_response(data=[t.to_dict() for t in todos])

@todo_bp.route("/pending", methods=["GET"])
def get_pending_todos():
    """Get all pending todos."""
    todos = services.filter_pending()
    return create_response(data=[t.to_dict() for t in todos])
