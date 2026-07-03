"""
Data models for the application.
"""
from dataclasses import dataclass
from typing import Optional

@dataclass
class Todo:
    """Todo data model."""
    id: int
    title: str
    description: Optional[str]
    status: str
    created_at: str
    updated_at: str

    def to_dict(self) -> dict:
        """Convert Todo instance to dictionary."""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "status": self.status,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }
