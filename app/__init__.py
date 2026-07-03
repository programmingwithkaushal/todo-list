"""
Main application factory module.
"""
from flask import Flask
from .database import init_db

def create_app(test_config=None) -> Flask:
    """Create and configure the Flask application."""
    app = Flask(__name__)

    if test_config is not None:
        app.config.update(test_config)

    with app.app_context():
        init_db()

    from .routes import todo_bp
    app.register_blueprint(todo_bp)

    return app
