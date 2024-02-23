class TaskManager():
    def __init__(self):
        self.tasks = {}
    
    def add_task(self):
        task_id = str(len(self.tasks) + 1)
        name = input("Type the name of the task you want to add: ")
        status = input("Type the status of the task (finished/unfinished): ")
        if status == "finished" or status == "unfinished":
            self.tasks[task_id] = { "name" : name, "status" : status}
        else:
            print(f"{status} not a valid option!")
        
    def show_tasks(self):
        print("List of tasks: ")
        for id, task in self.tasks.items():
            print(f"Task {id}: ")
            name_status = task["name"] + " - " +  task["status"]
            print(name_status)

task1 = TaskManager()
task1.add_task()
task1.add_task()
task1.show_tasks()