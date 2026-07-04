"""
Utility functions for the application.
"""

from typing import Any, Dict, Tuple

from flask import Response, jsonify


def create_response(
    data: Any = None, error: str = None, status_code: int = 200
) -> Tuple[Response, int]:
    """Create a standardized JSON response."""
    response: Dict[str, Any] = {}
    if data is not None:
        response["data"] = data
    if error is not None:
        response["error"] = error

    return jsonify(response), status_code
