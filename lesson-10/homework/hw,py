class Task:
  def __init__(self, task_title, description, due_date, status):
    self.title = task_title
    self.description = description
    self.due_date = due_date
    self.status = status
  def __str__(self):
    return f"Title: {self.title}, Description: {self.description}, Due Date: {self.due_date}, Status: {self.status}"
  
class ToDoList:
    def __init__(self):
        self.tasks = {}

    def add(self, task):
        self.tasks[task.title] = task
        print('\nA new task added successfully! 😊')

    def show_all_tasks(self):
        if not self.tasks:
            print('\nNo tasks available! :(')
            return
        for task_title, task in self.tasks.items():
            print(f'\n Title       : {task.title}')
            print(f' Description : {task.description}')
            print(f' Due Date    : {task.due_date}')
            print(f' Status      : {task.status}')
            print("-" * 32)

    def show_incomplete_tasks(self):
        found = False
        for task_title, task in self.tasks.items():
            if task.status == 'Pending':
                print(f'\n Title       : {task.title}')
                print(f' Description : {task.description}')
                print(f' Due Date    : {task.due_date}')
                print(f' Status      : {task.status}')
                print("-" * 32)
                found = True
        if not found:
            print('\nYou have no incomplete tasks, sir! :(')

    def finished(self, finished_title):
        for task_title, task in self.tasks.items():
            if task.title == finished_title:
                task.status = 'Completed'
                print(f"\n{task_title} is now marked as Completed! ❤️")



x = Task('Cooking', 'Cooking a spaghetti', '29-04-2025', "Pending")
x2 = Task('Play football', 'win a championship', '31-04-2025', "Pending")
x3 = Task('homework', 'finish homework', '30-04-2025', "Pending")
now = ToDoList()
now.show_all_tasks()
now.finished('homework')
now.show_incomplete_tasks()
