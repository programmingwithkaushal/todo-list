"""
Unit tests for database module.
"""

import sqlite3

from app.database import get_db_connection, init_db


def test_get_db_connection():
    """Test database connection."""
    conn = get_db_connection()
    assert isinstance(conn, sqlite3.Connection)
    conn.close()


def test_init_db():
    """Test database initialization."""
    init_db()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='todos'")
    table = cursor.fetchone()
    assert table is not None
    conn.close()
