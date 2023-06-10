from datetime import date

class Task():
    def __init__(self, title:str, description:str, due_date: date, finished:bool=None) -> None:
        self.title = title
        self.description = description
        self.due_date = due_date
        if finished:
            self.finished = finished
        else:
            self.finished = False
    
    def __str__(self) -> str:
        finished = True if self.finished else False
        return f"Title: {self.title}\nDescription: {self.description}\nDue Date: {self.due_date}\Finished: {finished}\n"
    
    def update_task_title(self, new_title:str) -> None:
        self.title = new_title

    def update_task_description(self, new_description:str) -> None:
        self.description = new_description

    def update_task_due_date(self, due_date: date) -> None:
        self.due_date = due_date
    
    def finish_task(self) -> None:
        self.finished = True
    
    def reopen_task(self) -> None:
        self.done = False