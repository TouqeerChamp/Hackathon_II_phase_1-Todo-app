"""
Task data model for the CLI Todo application.

This module defines the Task data structure with validation according to the
specification requirements.
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class Task:
    """
    Represents a single to-do item with id, title, description, and completion status.
    
    Attributes:
        id: Unique integer identifier for the task
        title: Required string title (1-200 characters)
        description: Optional string description
        completed: Boolean indicating completion status (default: False)
    """
    
    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False
    
    def __post_init__(self) -> None:
        """
        Validates the task attributes after initialization.
        
        Raises:
            ValueError: If any attribute doesn't meet the validation requirements
        """
        # Validate ID
        if not isinstance(self.id, int) or self.id <= 0:
            raise ValueError(f"Task ID must be a positive integer, got {self.id}")
        
        # Validate title
        if not isinstance(self.title, str):
            raise ValueError(f"Task title must be a string, got {type(self.title)}")
        
        if len(self.title) < 1 or len(self.title) > 200:
            raise ValueError(f"Task title must be between 1 and 200 characters, got {len(self.title)}")
        
        # Validate completed status
        if not isinstance(self.completed, bool):
            raise ValueError(f"Task completed status must be a boolean, got {type(self.completed)}")


def validate_task_title(title: str) -> bool:
    """
    Validates a task title according to the specification.
    
    Args:
        title: The title to validate
        
    Returns:
        True if the title is valid, False otherwise
    """
    if not isinstance(title, str):
        return False
    
    # Check length: 1-200 characters
    if len(title) < 1 or len(title) > 200:
        return False
    
    # Check if title is not just whitespace
    if title.strip() == "":
        return False
    
    return True