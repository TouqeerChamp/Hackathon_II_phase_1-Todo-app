"""
Task management service for the CLI Todo application.

This module provides in-memory storage and CRUD operations for tasks.
"""

from typing import List, Optional, Dict, Any
from src.models.task import Task, validate_task_title


class TaskManager:
    """
    Manages tasks in memory with CRUD operations and ID auto-increment functionality.
    """
    
    def __init__(self) -> None:
        """Initialize the task manager with an empty task list."""
        self._tasks: List[Task] = []
    
    def add_task(self, title: str, description: Optional[str] = None) -> Task:
        """
        Add a new task to the task list.
        
        Args:
            title: The task title (1-200 characters)
            description: Optional task description
            
        Returns:
            The newly created Task object with auto-assigned ID
            
        Raises:
            ValueError: If the title doesn't meet validation requirements
        """
        # Validate the title
        if not validate_task_title(title):
            raise ValueError(f"Invalid task title: '{title}'. Title must be 1-200 characters and not empty.")
        
        # Generate a new ID by finding the highest existing ID and incrementing
        new_id = self._get_next_id()
        
        # Create the new task
        task = Task(
            id=new_id,
            title=title,
            description=description,
            completed=False  # New tasks are not completed by default
        )
        
        # Add the task to the list
        self._tasks.append(task)
        
        return task
    
    def get_all_tasks(self) -> List[Task]:
        """
        Get all tasks in the task list.
        
        Returns:
            A list of all Task objects
        """
        return self._tasks.copy()  # Return a copy to prevent external modification
    
    def get_task_by_id(self, task_id: int) -> Optional[Task]:
        """
        Get a task by its ID.
        
        Args:
            task_id: The ID of the task to retrieve
            
        Returns:
            The Task object if found, None otherwise
        """
        for task in self._tasks:
            if task.id == task_id:
                return task
        return None
    
    def update_task(self, task_id: int, title: Optional[str] = None, description: Optional[str] = None) -> bool:
        """
        Update an existing task's title and/or description.
        
        Args:
            task_id: The ID of the task to update
            title: New title (optional, must be 1-200 characters if provided)
            description: New description (optional)
            
        Returns:
            True if the task was updated, False if the task was not found
        """
        task = self.get_task_by_id(task_id)
        if task is None:
            return False
        
        # If a new title is provided, validate it
        if title is not None:
            if not validate_task_title(title):
                raise ValueError(f"Invalid task title: '{title}'. Title must be 1-200 characters and not empty.")
            task.title = title
        
        # If a new description is provided, update it
        if description is not None:
            task.description = description
        
        return True
    
    def toggle_task_completion(self, task_id: int) -> bool:
        """
        Toggle the completion status of a task.
        
        Args:
            task_id: The ID of the task to toggle
            
        Returns:
            True if the task status was toggled, False if the task was not found
        """
        task = self.get_task_by_id(task_id)
        if task is None:
            return False
        
        task.completed = not task.completed
        return True
    
    def delete_task(self, task_id: int) -> bool:
        """
        Delete a task by its ID.
        
        Args:
            task_id: The ID of the task to delete
            
        Returns:
            True if the task was deleted, False if the task was not found
        """
        task = self.get_task_by_id(task_id)
        if task is None:
            return False
        
        self._tasks.remove(task)
        return True
    
    def _get_next_id(self) -> int:
        """
        Get the next available ID by finding the highest existing ID and incrementing.
        
        Returns:
            The next available ID
        """
        if not self._tasks:
            return 1
        
        # Find the highest ID currently in use
        max_id = max(task.id for task in self._tasks)
        return max_id + 1