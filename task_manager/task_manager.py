from task_manager.task import Task
from task_manager.task_manager import TaskManager


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


