# Data Model: CLI Todo App - Phase I

## Task Entity

### Fields
- **id**: `int` (auto-increment, unique)
  - Validation: Must be a positive integer
  - Auto-generated when a new task is created
- **title**: `str` (required, 1-200 characters)
  - Validation: Must be 1-200 characters long, not empty
- **description**: `str` (optional)
  - Validation: Can be empty or any length up to system limits
- **completed**: `bool`
  - Default value: `False`
  - Validation: Must be a boolean value

### Example
```python
task = {
    "id": 1,
    "title": "Complete project documentation",
    "description": "Write comprehensive docs for the project",
    "completed": False
}
```

## Task List Entity

### Fields
- **tasks**: `List[Task]` (collection of task dictionaries)
  - Validation: Contains only valid Task entities
  - Operations: Add, remove, update, find by ID

## Validation Rules

### Title Validation
- Minimum length: 1 character
- Maximum length: 200 characters
- Cannot be empty or whitespace-only

### ID Validation
- Must be a positive integer
- Must be unique within the task list
- Auto-incremented from the highest existing ID

### Completed Status Validation
- Must be a boolean value (True or False)
- Default value is False when creating a new task

## State Transitions

### Task Completion
- Initial state: `completed = False`
- Transition: User marks task as complete
- Final state: `completed = True`

### Task Update
- Initial state: Task exists with certain values
- Transition: User updates title or description
- Final state: Task has updated values, other fields unchanged

## Relationships

- The Task List contains multiple Task entities
- Each Task has a unique ID within the Task List
- No other relationships exist in this model