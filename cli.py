# cli.py

from task import Task
from database import Database
from datetime import datetime

class TaskManagerCLI:
    def __init__(self):
        self.db = Database()

    def run(self):
        while True:
            print("\nTask Manager")
            print("1. Add a new task")
            print("2. Edit a task")
            print("3. Mark a task as completed")
            print("4. List all tasks")
            print("5. Filter tasks")
            print("6. Generate reports")
            print("7. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.edit_task()
            elif choice == "3":
                self.mark_completed()
            elif choice == "4":
                self.list_tasks()
            elif choice == "5":
                self.filter_tasks()
            elif choice == "6":
                self.generate_reports()
            elif choice == "7":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 7.")

    def add_task(self):
        title = input("Enter task title: ")
        description = input("Enter task description: ")
        deadline = input("Enter task deadline (YYYY-MM-DD): ")
        priority = int(input("Enter task priority (1 - High, 2 - Medium, 3 - Low): "))
        task = Task(title, description, deadline, priority)
        self.db.add_task(task)
        print("Task added successfully.")

    def edit_task(self):
        task_id = int(input("Enter task ID to edit: "))
        # Fetch task details from DB based on task_id, update fields, and save changes

    def mark_completed(self):
        task_id = int(input("Enter task ID to mark as completed: "))
        # Fetch task details from DB based on task_id, mark task as completed, and save changes

    def list_tasks(self):
        tasks = self.db.get_all_tasks()
        if tasks:
            for task in tasks:
                print(f"ID: {task.id}, Title: {task.title}, Priority: {task.priority}, Deadline: {task.deadline}, Completed: {task.completed}")
        else:
            print("No tasks found.")

    def filter_tasks(self):
        choice = input("Enter filter type (1 - Status, 2 - Priority, 3 - Deadline range): ")
        # Implement filtering logic based on user choice

    def generate_reports(self):
        choice = input("Enter report type (1 - Tasks completed this week, 2 - Overdue tasks): ")
        # Implement report generation logic based on user choice

    def __del__(self):
        self.db.close()
