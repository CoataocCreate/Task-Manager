# database.py

import sqlite3
from task import Task

class Database:
    def __init__(self, db_name="tasks.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                description TEXT,
                deadline TEXT,
                priority INTEGER,
                completed INTEGER
            )
        """)
        self.conn.commit()

    def add_task(self, task):
        self.cursor.execute("""
            INSERT INTO tasks (title, description, deadline, priority, completed)
            VALUES (?, ?, ?, ?, ?)
        """, (task.title, task.description, task.deadline, task.priority, 0))
        self.conn.commit()

    def get_all_tasks(self):
        self.cursor.execute("SELECT * FROM tasks")
        tasks = []
        for row in self.cursor.fetchall():
            task = Task(row[1], row[2], row[3], row[4])
            task.completed = True if row[5] == 1 else False
            tasks.append(task)
        return tasks

    def update_task(self, task):
        self.cursor.execute("""
            UPDATE tasks
            SET title=?, description=?, deadline=?, priority=?, completed=?
            WHERE id=?
        """, (task.title, task.description, task.deadline, task.priority, 1 if task.completed else 0, task.id))
        self.conn.commit()

    def delete_task(self, task_id):
        self.cursor.execute("DELETE FROM tasks WHERE id=?", (task_id,))
        self.conn.commit()

    def close(self):
        self.conn.close()
