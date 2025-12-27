# API Contracts: CLI Todo App - Phase I

## Overview
This document defines the functional contracts for the CLI Todo application. Since this is a command-line interface application, the "contracts" represent the functional interfaces and expected behaviors rather than traditional API endpoints.

## Task Management Contracts

### Add Task
- **Input**: title (str, 1-200 chars), description (str, optional)
- **Output**: success message with new task ID or error message
- **Behavior**: Creates a new task with auto-generated ID and 'completed' status as False
- **Validation**: Title must be 1-200 characters, not empty
- **Success Response**: "Task added successfully with ID: {id}"
- **Error Response**: "Error: {error_message}"

### View Tasks
- **Input**: None
- **Output**: Formatted list of all tasks with status indicators
- **Behavior**: Displays all tasks with [ ] for incomplete and [✓] for complete
- **Success Response**: Formatted task list or "No tasks found."
- **Error Response**: N/A

### Update Task
- **Input**: task ID (int), new title (str, optional), new description (str, optional)
- **Output**: success confirmation or error message
- **Behavior**: Updates title and/or description of existing task
- **Validation**: Task ID must exist, title (if provided) must be 1-200 characters
- **Success Response**: "Task updated successfully"
- **Error Response**: "Error: {error_message}"

### Mark Complete/Incomplete
- **Input**: task ID (int)
- **Output**: success confirmation or error message
- **Behavior**: Toggles the completion status of the specified task
- **Validation**: Task ID must exist
- **Success Response**: "Task {id} marked as {complete/incomplete}"
- **Error Response**: "Error: {error_message}"

### Delete Task
- **Input**: task ID (int)
- **Output**: confirmation prompt and success/error message
- **Behavior**: Removes task from the list after user confirmation
- **Validation**: Task ID must exist
- **Success Response**: "Task {id} deleted successfully"
- **Error Response**: "Error: {error_message}"

## User Interface Contracts

### Main Menu
- **Output**: Displays numbered options for all available operations
- **Behavior**: Presents clear options to the user and processes selected input
- **Response**: Processes the selected option or displays error for invalid input

### Input Validation
- **Behavior**: Validates all user inputs according to defined rules
- **Response**: Provides clear error messages for invalid inputs
- **Validation Rules**:
  - Menu options: Must be valid number in the displayed range
  - Task titles: 1-200 characters, not empty
  - Task IDs: Must be positive integers that exist in the task list
  - Descriptions: Any length (optional field)

## Error Handling Contracts

### Input Errors
- **Scenario**: User provides invalid input
- **Response**: Clear error message and prompt to try again

### Business Logic Errors
- **Scenario**: Operation cannot be completed (e.g., task ID doesn't exist)
- **Response**: Descriptive error message explaining why the operation failed

### System Errors
- **Scenario**: Unexpected system issue
- **Response**: Graceful error handling with user-friendly message