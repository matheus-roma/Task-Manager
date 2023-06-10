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
        print("=====")
        if not self.tasks:
            print("No tasks founded")
            print("=====")
        else:
            for task in self.tasks:
                print(task)
            print("=====")

def main():
    print("Main being executed")


if __name__ == '__main__':
    main()