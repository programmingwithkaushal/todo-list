"""
Database connection and initialization module.
"""

import os
import sqlite3


def get_db_connection() -> sqlite3.Connection:
    """Create and return a database connection."""
    database_url = os.environ.get("DATABASE_URL", "todos.db")
    conn = sqlite3.connect(database_url)
    conn.row_factory = sqlite3.Row
    return conn


def init_db() -> None:
    """Initialize the database with the required tables."""
    conn = get_db_connection()
    with conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS todos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT,
                status TEXT NOT NULL DEFAULT 'pending',
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """
        )
    conn.close()
