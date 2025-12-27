# Quickstart Guide: CLI Todo App - Phase I

## Getting Started

This guide will help you run the CLI Todo application on your local machine.

### Prerequisites

- Python 3.13 or higher
- No external dependencies required (uses only standard library)

### Installation

1. Clone or download the repository
2. Navigate to the project root directory
3. Ensure you have Python 3.13+ installed:
   ```bash
   python --version
   ```

### Running the Application

1. Navigate to the project root directory
2. Run the main application file:
   ```bash
   python src/todo_app.py
   ```
3. The application will start with a welcome message and display the main menu

### Using the Application

Once the application is running, you'll see a menu with the following options:

1. **Add Task**: Creates a new task with a title and optional description
2. **View Tasks**: Displays all tasks with their completion status ([ ] or [✓])
3. **Update Task**: Modifies the title or description of an existing task
4. **Mark Complete/Incomplete**: Toggles the completion status of a task
5. **Delete Task**: Removes a task from the list (with confirmation)
6. **Exit**: Terminates the application

### Example Usage

```
Welcome to the Todo App!
Please select an option:
1. Add Task
2. View Tasks
3. Update Task
4. Mark Complete/Incomplete
5. Delete Task
6. Exit

> 1
Enter task title: Buy groceries
Enter task description (optional): Need to buy milk and bread
Task added successfully with ID: 1

> 2
Tasks:
[ ] 1. Buy groceries - Need to buy milk and bread

> 4
Enter task ID to mark complete/incomplete: 1
Task 1 marked as complete

> 2
Tasks:
[✓] 1. Buy groceries - Need to bread
```

### Important Notes

- All data is stored in memory only and will be lost when the application exits
- Task titles must be between 1 and 200 characters
- Task IDs are auto-generated as unique integers
- The application validates all user inputs and provides appropriate error messages