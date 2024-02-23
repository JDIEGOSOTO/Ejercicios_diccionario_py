class ActividadesDiarias():
    def __init__(self):
        self.activities = {}

    def add_activity(self):
        activity_id = str(len(self.activities) + 1)
        nombre = input("Type the name of the activity: ")
        fecha = input("Type the date of the activity: ")
        duracion = input("Type the duration of the activity: ")
        self.activities[activity_id] = { "name" : nombre, "fecha" : fecha, "duracion" : duracion }

    def show_activities(self):
        print("List of activities: ")
        for id, activity in self.activities.items():
            print(f"Activity {id}: ")
            activity_info = f"Name: {activity["name"].title()}, Date: {activity["fecha"]}, Duration: {activity["duracion"]}"
            print(activity_info)

activity1 = ActividadesDiarias()
activity1.add_activity()
activity1.show_activities()