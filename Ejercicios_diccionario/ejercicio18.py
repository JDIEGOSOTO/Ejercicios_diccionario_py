class TrackerHabits():
    def __init__(self):
        self.habits = {}
    
    def add_habit(self):
        habit_id = str(len(self.habits) + 1)
        nombre = input("Type the name of the habit: ")
        date = input("Type the date of the habit: ")
        status = input("Did you completed the habit? (yes/no): ")
        if status == "yes":
            self.habits[habit_id] = { "name": nombre, "date" : date, "status" : "completed" }
        elif status == "no":
            self.habits[habit_id] = { "name": nombre, "date" : date, "status" : "not completed" }

    def show_habits(self):
        print("Lis of Habits: ")
        for id, habit in self.habits.items():
            print(f"Habit {id}: ")
            habit_info = f"Name: {habit["name"].title()}, Date: {habit["date"]}, status: {habit["status"].title()}"
            print(habit_info)

habit = TrackerHabits()
habit.add_habit()
habit.show_habits()