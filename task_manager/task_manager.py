from task_manager import Task
from datetime import date

class TaskManager:
    def __init__(self) -> None:
        self.tasks = []
    
    def add_task(self, task) -> None:
        self.tasks.append(task)

    def delete_task(self, task: Task) ->None:
        if task in self.tasks:
            self.tasks.remove(task)

    def show_tasks(self) -> None:
        if not self.tasks:
            print("No tasks founded")
        else:
            for task in self.tasks:
                print(task)
            print("===")

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