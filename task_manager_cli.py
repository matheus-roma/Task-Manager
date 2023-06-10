#!/usr/bin/env python3

from task_manager.task_manager import TaskManager
from task_manager.task import Task
from datetime import date



def main():
    task_manager = TaskManager()

    task1 = Task("Finish homework", "Complete math exercises", date(2023, 6, 15))
    task2 = Task("Buy groceries", "Get milk, eggs, and bread", date(2023, 6, 10))

    task_manager.add_task(task1)
    task_manager.add_task(task2)

    task_manager.show_tasks()

    task1.finish_task()

    task_manager.show_tasks()


if __name__ == '__main__':
    main()
