"""
Unit tests for the TaskManager class.

This module tests all CRUD operations and functionality of the TaskManager.
"""

import unittest
from src.services.task_manager import TaskManager
from src.models.task import Task, validate_task_title


class TestTaskManager(unittest.TestCase):
    """Test cases for the TaskManager class."""

    def setUp(self) -> None:
        """Set up a fresh TaskManager instance for each test."""
        self.task_manager = TaskManager()

    def test_add_task_success(self) -> None:
        """Test adding a task successfully."""
        title = "Test Task"
        description = "Test Description"
        
        task = self.task_manager.add_task(title, description)
        
        # Check that the task was returned correctly
        self.assertIsInstance(task, Task)
        self.assertEqual(task.title, title)
        self.assertEqual(task.description, description)
        self.assertFalse(task.completed)
        self.assertEqual(task.id, 1)  # First task should have ID 1
        
        # Check that the task was added to the manager
        tasks = self.task_manager.get_all_tasks()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0], task)

    def test_add_task_without_description(self) -> None:
        """Test adding a task without a description."""
        title = "Test Task"
        
        task = self.task_manager.add_task(title)
        
        self.assertEqual(task.title, title)
        self.assertIsNone(task.description)
        self.assertFalse(task.completed)
        self.assertEqual(task.id, 1)

    def test_add_task_with_invalid_title(self) -> None:
        """Test adding a task with an invalid title raises ValueError."""
        # Test with empty title
        with self.assertRaises(ValueError):
            self.task_manager.add_task("")
        
        # Test with title too long (over 200 characters)
        long_title = "a" * 201
        with self.assertRaises(ValueError):
            self.task_manager.add_task(long_title)
        
        # Test with title that's just whitespace
        with self.assertRaises(ValueError):
            self.task_manager.add_task("   ")

    def test_get_all_tasks_empty(self) -> None:
        """Test getting all tasks when the manager is empty."""
        tasks = self.task_manager.get_all_tasks()
        
        self.assertEqual(len(tasks), 0)
        self.assertEqual(tasks, [])

    def test_get_all_tasks_with_tasks(self) -> None:
        """Test getting all tasks when the manager has tasks."""
        # Add some tasks
        task1 = self.task_manager.add_task("Task 1")
        task2 = self.task_manager.add_task("Task 2", "Description for task 2")
        
        tasks = self.task_manager.get_all_tasks()
        
        self.assertEqual(len(tasks), 2)
        self.assertIn(task1, tasks)
        self.assertIn(task2, tasks)
        
        # Verify that the returned list is a copy (not the internal list)
        self.assertIsNot(tasks, self.task_manager._tasks)

    def test_get_task_by_id_found(self) -> None:
        """Test getting a task by ID when it exists."""
        # Add a task
        original_task = self.task_manager.add_task("Test Task")
        task_id = original_task.id
        
        # Retrieve the task by ID
        retrieved_task = self.task_manager.get_task_by_id(task_id)
        
        self.assertIsNotNone(retrieved_task)
        self.assertEqual(retrieved_task, original_task)

    def test_get_task_by_id_not_found(self) -> None:
        """Test getting a task by ID when it doesn't exist."""
        # Try to get a task with an ID that doesn't exist
        retrieved_task = self.task_manager.get_task_by_id(999)
        
        self.assertIsNone(retrieved_task)

    def test_update_task_success(self) -> None:
        """Test updating a task successfully."""
        # Add a task
        original_task = self.task_manager.add_task("Original Title", "Original Description")
        task_id = original_task.id
        
        # Update the task
        new_title = "Updated Title"
        new_description = "Updated Description"
        result = self.task_manager.update_task(task_id, new_title, new_description)
        
        # Verify the update was successful
        self.assertTrue(result)
        
        # Verify the task was updated
        updated_task = self.task_manager.get_task_by_id(task_id)
        self.assertIsNotNone(updated_task)
        self.assertEqual(updated_task.title, new_title)
        self.assertEqual(updated_task.description, new_description)
        self.assertEqual(updated_task.id, task_id)  # ID should remain the same

    def test_update_task_partial(self) -> None:
        """Test updating only the title or description of a task."""
        # Add a task
        original_task = self.task_manager.add_task("Original Title", "Original Description")
        task_id = original_task.id
        
        # Update only the title
        new_title = "Updated Title"
        result = self.task_manager.update_task(task_id, title=new_title)
        
        self.assertTrue(result)
        
        updated_task = self.task_manager.get_task_by_id(task_id)
        self.assertIsNotNone(updated_task)
        self.assertEqual(updated_task.title, new_title)
        self.assertEqual(updated_task.description, "Original Description")  # Should remain unchanged
        
        # Reset for next test
        original_task = self.task_manager.add_task("Original Title 2", "Original Description 2")
        task_id = original_task.id
        
        # Update only the description
        new_description = "Updated Description"
        result = self.task_manager.update_task(task_id, description=new_description)
        
        self.assertTrue(result)
        
        updated_task = self.task_manager.get_task_by_id(task_id)
        self.assertIsNotNone(updated_task)
        self.assertEqual(updated_task.title, "Original Title 2")  # Should remain unchanged
        self.assertEqual(updated_task.description, new_description)

    def test_update_task_invalid_title(self) -> None:
        """Test updating a task with an invalid title raises ValueError."""
        # Add a task
        original_task = self.task_manager.add_task("Original Title")
        task_id = original_task.id
        
        # Try to update with an invalid title
        with self.assertRaises(ValueError):
            self.task_manager.update_task(task_id, title="")  # Empty title
        
        # Try to update with a title that's too long
        with self.assertRaises(ValueError):
            self.task_manager.update_task(task_id, title="a" * 201)  # Too long

    def test_update_task_not_found(self) -> None:
        """Test updating a task that doesn't exist."""
        result = self.task_manager.update_task(999, "New Title")
        
        self.assertFalse(result)

    def test_toggle_task_completion(self) -> None:
        """Test toggling a task's completion status."""
        # Add a task (should be incomplete by default)
        task = self.task_manager.add_task("Test Task")
        task_id = task.id
        
        # Verify it starts as incomplete
        self.assertFalse(task.completed)
        
        # Toggle completion status
        result = self.task_manager.toggle_task_completion(task_id)
        
        # Verify the toggle was successful
        self.assertTrue(result)
        
        # Verify the task is now complete
        toggled_task = self.task_manager.get_task_by_id(task_id)
        self.assertIsNotNone(toggled_task)
        self.assertTrue(toggled_task.completed)
        
        # Toggle again to make it incomplete
        result = self.task_manager.toggle_task_completion(task_id)
        self.assertTrue(result)
        
        # Verify the task is now incomplete again
        toggled_task = self.task_manager.get_task_by_id(task_id)
        self.assertIsNotNone(toggled_task)
        self.assertFalse(toggled_task.completed)

    def test_toggle_task_completion_not_found(self) -> None:
        """Test toggling completion status for a task that doesn't exist."""
        result = self.task_manager.toggle_task_completion(999)
        
        self.assertFalse(result)

    def test_delete_task_success(self) -> None:
        """Test deleting a task successfully."""
        # Add a task
        task = self.task_manager.add_task("Test Task")
        task_id = task.id
        
        # Verify the task exists
        self.assertEqual(len(self.task_manager.get_all_tasks()), 1)
        
        # Delete the task
        result = self.task_manager.delete_task(task_id)
        
        # Verify the deletion was successful
        self.assertTrue(result)
        
        # Verify the task is gone
        self.assertEqual(len(self.task_manager.get_all_tasks()), 0)
        self.assertIsNone(self.task_manager.get_task_by_id(task_id))

    def test_delete_task_not_found(self) -> None:
        """Test deleting a task that doesn't exist."""
        result = self.task_manager.delete_task(999)
        
        self.assertFalse(result)

    def test_id_auto_increment(self) -> None:
        """Test that task IDs are auto-incremented correctly."""
        # Add several tasks
        task1 = self.task_manager.add_task("Task 1")
        task2 = self.task_manager.add_task("Task 2")
        task3 = self.task_manager.add_task("Task 3")
        
        # Verify IDs are sequential starting from 1
        self.assertEqual(task1.id, 1)
        self.assertEqual(task2.id, 2)
        self.assertEqual(task3.id, 3)
        
        # Delete a task in the middle
        self.task_manager.delete_task(2)
        
        # Add another task - it should get the next available ID
        task4 = self.task_manager.add_task("Task 4")
        self.assertEqual(task4.id, 4)


class TestValidateTaskTitle(unittest.TestCase):
    """Test cases for the validate_task_title function."""
    
    def test_valid_titles(self) -> None:
        """Test that valid titles return True."""
        # Valid titles
        valid_titles = [
            "A",  # Minimum length
            "A" * 200,  # Maximum length
            "Normal title",
            "12345",
            "Title with spaces and symbols!",
        ]
        
        for title in valid_titles:
            with self.subTest(title=title):
                self.assertTrue(validate_task_title(title))
    
    def test_invalid_titles(self) -> None:
        """Test that invalid titles return False."""
        # Invalid titles
        invalid_titles = [
            "",  # Empty
            "A" * 201,  # Too long
            "   ",  # Only whitespace
            "\t\n",  # Only whitespace characters
        ]
        
        for title in invalid_titles:
            with self.subTest(title=title):
                self.assertFalse(validate_task_title(title))
    
    def test_non_string_titles(self) -> None:
        """Test that non-string inputs return False."""
        non_strings = [
            123,
            None,
            [],
            {},
            True,
        ]
        
        for title in non_strings:
            with self.subTest(title=title):
                self.assertFalse(validate_task_title(title))  # type: ignore


if __name__ == '__main__':
    unittest.main()