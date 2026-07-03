"""
Business logic and database operations.
"""
import sqlite3
from typing import List, Optional
from .database import get_db_connection
from .models import Todo

def dict_to_todo(row: sqlite3.Row) -> Todo:
    """Convert database row to Todo object."""
    return Todo(
        id=row["id"],
        title=row["title"],
        description=row["description"],
        status=row["status"],
        created_at=row["created_at"],
        updated_at=row["updated_at"],
    )

def create_todo(title: str, description: Optional[str] = None) -> Todo:
    """Create a new todo."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO todos (title, description, status) VALUES (?, ?, 'pending')",
        (title, description),
    )
    todo_id = cursor.lastrowid
    conn.commit()

    cursor.execute("SELECT * FROM todos WHERE id = ?", (todo_id,))
    row = cursor.fetchone()
    conn.close()

    return dict_to_todo(row)

def get_all_todos() -> List[Todo]:
    """Retrieve all todos."""
    conn = get_db_connection()
    cursor = conn.execute("SELECT * FROM todos")
    rows = cursor.fetchall()
    conn.close()
    return [dict_to_todo(row) for row in rows]

def get_todo_by_id(todo_id: int) -> Optional[Todo]:
    """Retrieve a single todo by ID."""
    conn = get_db_connection()
    cursor = conn.execute("SELECT * FROM todos WHERE id = ?", (todo_id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return dict_to_todo(row)
    return None

def update_todo(todo_id: int, title: str, description: Optional[str], status: str) -> Optional[Todo]:
    """Update an existing todo."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        UPDATE todos 
        SET title = ?, description = ?, status = ?, updated_at = CURRENT_TIMESTAMP
        WHERE id = ?
        """,
        (title, description, status, todo_id),
    )
    conn.commit()

    cursor.execute("SELECT * FROM todos WHERE id = ?", (todo_id,))
    row = cursor.fetchone()
    conn.close()

    if row:
        return dict_to_todo(row)
    return None

def delete_todo(todo_id: int) -> bool:
    """Delete a todo."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM todos WHERE id = ?", (todo_id,))
    deleted = cursor.rowcount > 0
    conn.commit()
    conn.close()
    return deleted

def complete_todo(todo_id: int) -> Optional[Todo]:
    """Mark a todo as completed."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        UPDATE todos 
        SET status = 'completed', updated_at = CURRENT_TIMESTAMP
        WHERE id = ?
        """,
        (todo_id,),
    )
    conn.commit()

    cursor.execute("SELECT * FROM todos WHERE id = ?", (todo_id,))
    row = cursor.fetchone()
    conn.close()

    if row:
        return dict_to_todo(row)
    return None

def search_todos(query: str) -> List[Todo]:
    """Search todos by title or description."""
    conn = get_db_connection()
    search_query = f"%{query}%"
    cursor = conn.execute(
        "SELECT * FROM todos WHERE title LIKE ? OR description LIKE ?",
        (search_query, search_query),
    )
    rows = cursor.fetchall()
    conn.close()
    return [dict_to_todo(row) for row in rows]

def filter_completed() -> List[Todo]:
    """Get all completed todos."""
    conn = get_db_connection()
    cursor = conn.execute("SELECT * FROM todos WHERE status = 'completed'")
    rows = cursor.fetchall()
    conn.close()
    return [dict_to_todo(row) for row in rows]

def filter_pending() -> List[Todo]:
    """Get all pending todos."""
    conn = get_db_connection()
    cursor = conn.execute("SELECT * FROM todos WHERE status = 'pending'")
    rows = cursor.fetchall()
    conn.close()
    return [dict_to_todo(row) for row in rows]
