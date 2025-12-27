"""
Main entry point for the CLI Todo application.

This module implements the main application loop with menu navigation.
"""

from src.services.task_manager import TaskManager
from src.ui.cli_interface import (
    display_tasks, get_task_input, get_task_id, confirm_deletion,
    display_menu, get_menu_choice, display_add_success, display_update_success,
    display_toggle_success, display_delete_success, display_error
)


def main() -> None:
    """Main application entry point."""
    print("Welcome to the Todo App!")
    
    # Initialize the task manager
    task_manager = TaskManager()
    
    # Main application loop
    while True:
        display_menu()
        choice = get_menu_choice()
        
        if choice == 1:
            # Add Task
            try:
                title, description = get_task_input()
                task = task_manager.add_task(title, description)
                display_add_success(task)
            except ValueError as e:
                display_error(str(e))
        
        elif choice == 2:
            # View Tasks
            display_tasks(task_manager)
        
        elif choice == 3:
            # Update Task
            task_id = get_task_id()
            if task_id is not None:
                task = task_manager.get_task_by_id(task_id)
                if task:
                    print(f"Current task: {task.title}")
                    new_title_input = input(f"Enter new title (current: '{task.title}', press Enter to keep current): ").strip()
                    new_title = new_title_input if new_title_input else None
                    
                    new_desc_input = input(f"Enter new description (current: '{task.description}', press Enter to keep current): ").strip()
                    new_description = new_desc_input if new_desc_input != "" else None  # Allow empty description
                    
                    try:
                        if task_manager.update_task(task_id, new_title, new_description):
                            display_update_success()
                        else:
                            display_error("Failed to update task")
                    except ValueError as e:
                        display_error(str(e))
                else:
                    display_error(f"Task with ID {task_id} not found")
        
        elif choice == 4:
            # Mark Complete/Incomplete
            task_id = get_task_id()
            if task_id is not None:
                if task_manager.toggle_task_completion(task_id):
                    task = task_manager.get_task_by_id(task_id)
                    if task:
                        display_toggle_success(task_id, task.completed)
                else:
                    display_error(f"Task with ID {task_id} not found")
        
        elif choice == 5:
            # Delete Task
            task_id = get_task_id()
            if task_id is not None:
                task = task_manager.get_task_by_id(task_id)
                if task:
                    if confirm_deletion(task_id):
                        if task_manager.delete_task(task_id):
                            display_delete_success(task_id)
                        else:
                            display_error("Failed to delete task")
                    else:
                        print("Deletion cancelled.")
                else:
                    display_error(f"Task with ID {task_id} not found")
        
        elif choice == 6:
            # Exit
            print("Goodbye!")
            break
        
        else:
            if choice is not None:  # Only show error if it was a number but not 1-6
                print("Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()