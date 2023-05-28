from datetime import date

class Task():
    def __init__(self, title:str, description:str, year:int, month:int, day:int, priority:int, done:bool=None) -> None:
        self.title = title
        self.description = description
        self.due_date = date(year, month, day)
        self.priority = priority
        if done == True:
            self.done = done
        else:
            self.done = False
    
    def update_task_title(self, new_title:str) -> None:
        self.title = new_title

    def update_task_description(self, new_description:str) -> None:
        self.description = new_description

    def update_task_due_date(self, new_year:int, new_month:int, new_day:int) -> None:
        self.due_date = date(new_year, new_month, new_day)
    
    def finish_task(self) -> None:
        self.done = True
    
    def reopen_task(self) -> None:
        self.done = False



# result = date(year=2020, month=1, day=31)
# print(type(result))

#task = Task("Create a class", "Create a class in python", 2023, 5, 28, 5)

