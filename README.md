# CLI Todo App

A command-line interface (CLI) application for managing to-do tasks. This application allows users to create, view, update, mark complete/incomplete, and delete tasks through a simple text-based menu interface.

## Features

- Add new tasks with titles and optional descriptions
- View all tasks with their completion status
- Update existing task titles and descriptions
- Mark tasks as complete or incomplete
- Delete tasks with confirmation
- Simple, intuitive menu-driven interface

## Prerequisites

- Python 3.13 or higher

## Installation

1. Clone or download this repository
2. Navigate to the project root directory
3. Ensure you have Python 3.13+ installed:
   ```bash
   python --version
   ```

## Usage

To run the application, execute the following command from the project root directory:

```bash
python src/todo_app.py
```

The application will start with a welcome message and display the main menu with the following options:

1. **Add Task**: Creates a new task with a title and optional description
2. **View Tasks**: Displays all tasks with their completion status ([ ] or [✓])
3. **Update Task**: Modifies the title or description of an existing task
4. **Mark Complete/Incomplete**: Toggles the completion status of a task
5. **Delete Task**: Removes a task from the list (with confirmation)
6. **Exit**: Terminates the application

## Example Usage

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

## Project Structure

```
src/
├── todo_app.py          # Main application entry point with CLI loop
├── models/
│   └── task.py          # Task data model with validation
├── services/
│   └── task_manager.py  # Task management logic (CRUD operations)
└── ui/
    └── cli_interface.py # CLI interface and user interaction logic

tests/
├── unit/
│   ├── test_task.py     # Task model tests
│   └── test_task_manager.py # Task manager tests
└── integration/
    └── test_cli_flow.py # CLI flow integration tests
```

## Important Notes

- All data is stored in memory only and will be lost when the application exits
- Task titles must be between 1 and 200 characters
- Task IDs are auto-generated as unique integers
- The application validates all user inputs and provides appropriate error messages

## Running Tests

To run the unit tests:

```bash
python -m unittest tests/unit/test_task_manager.py -v
```

## License

This project is open source and available under the [MIT License](LICENSE).