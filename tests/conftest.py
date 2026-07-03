"""
Pytest configuration and fixtures.
"""
import os
import tempfile
import pytest
from app import create_app
from app.database import init_db

@pytest.fixture(autouse=True)
def setup_database():
    """Setup a temporary database for testing."""
    db_fd, db_path = tempfile.mkstemp()
    os.environ["DATABASE_URL"] = db_path

    init_db()

    yield

    os.close(db_fd)
    os.unlink(db_path)

@pytest.fixture
def client():
    """Create a test client for the app."""
    app = create_app({"TESTING": True})
    with app.test_client() as client:
        yield client
