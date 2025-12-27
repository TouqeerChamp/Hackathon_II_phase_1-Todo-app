"""
CLI interface module for the Todo application.

This module provides functions for user interaction through the command line.
"""

from typing import Optional
from src.services.task_manager import TaskManager
from src.models.task import Task


def display_tasks(task_manager: TaskManager) -> None:
    """
    Display all tasks with their completion status.
    
    Args:
        task_manager: The TaskManager instance to retrieve tasks from
    """
    tasks = task_manager.get_all_tasks()
    
    if not tasks:
        print("No tasks found.")
        return
    
    print("Tasks:")
    for task in tasks:
        status = "[✓]" if task.completed else "[ ]"
        description = f" - {task.description}" if task.description else ""
        print(f"{status} {task.id}. {task.title}{description}")


def get_task_input() -> tuple[str, Optional[str]]:
    """
    Get task input from the user.
    
    Returns:
        A tuple containing the title and optional description
    """
    title = input("Enter task title: ").strip()
    
    description_input = input("Enter task description (optional, press Enter to skip): ").strip()
    description = description_input if description_input else None
    
    return title, description


def get_task_id() -> Optional[int]:
    """
    Get a task ID from user input.
    
    Returns:
        The task ID if valid, None if invalid
    """
    try:
        task_id_input = input("Enter task ID: ").strip()
        return int(task_id_input)
    except ValueError:
        print("Invalid task ID. Please enter a number.")
        return None


def confirm_deletion(task_id: int) -> bool:
    """
    Ask the user for confirmation before deleting a task.
    
    Args:
        task_id: The ID of the task to be deleted
        
    Returns:
        True if the user confirms deletion, False otherwise
    """
    confirmation = input(f"Are you sure you want to delete task #{task_id}? (y/N): ").strip().lower()
    return confirmation in ['y', 'yes']


def display_menu() -> None:
    """Display the main menu options."""
    print("\nPlease select an option:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Mark Complete/Incomplete")
    print("5. Delete Task")
    print("6. Exit")


def get_menu_choice() -> Optional[int]:
    """
    Get the user's menu choice.
    
    Returns:
        The menu choice as an integer if valid, None if invalid
    """
    try:
        choice = input("Enter your choice (1-6): ").strip()
        return int(choice)
    except ValueError:
        print("Invalid choice. Please enter a number between 1 and 6.")
        return None


def display_add_success(task: Task) -> None:
    """
    Display a success message after adding a task.
    
    Args:
        task: The task that was added
    """
    print(f"Task added successfully with ID: {task.id}")


def display_update_success() -> None:
    """Display a success message after updating a task."""
    print("Task updated successfully")


def display_toggle_success(task_id: int, completed: bool) -> None:
    """
    Display a success message after toggling task completion status.
    
    Args:
        task_id: The ID of the task that was toggled
        completed: The new completion status
    """
    status = "complete" if completed else "incomplete"
    print(f"Task {task_id} marked as {status}")


def display_delete_success(task_id: int) -> None:
    """
    Display a success message after deleting a task.
    
    Args:
        task_id: The ID of the task that was deleted
    """
    print(f"Task {task_id} deleted successfully")


def display_error(message: str) -> None:
    """
    Display an error message.
    
    Args:
        message: The error message to display
    """
    print(f"Error: {message}")