class EventDesigner():
    def __init__(self):
        self.events = {}

    def add_event(self):
        event_id = str(len(self.events) + 1)
        name = input("Type the name of the event: ")
        date = input("Type the date of the event: ")
        hour = input("Type the hour of the event: ")
        participants = int(input("How many participants will be at the event?"))
        self.events[event_id] = { "name" : name, "date" : date, "hour" : hour, "participants" : participants }

    def show_events(self):
        print("Lis of Events: ")
        for id, event in self.events.items():
            print(f"Event {id}: ")
            event_info = f"Name: {event["name"].title()}, Date: {event["date"]}, Hour: {event["hour"]}, Numer of Participants{event["participants"]} "
            print(event_info)


events1 = EventDesigner()
events1.add_event()
events1.show_events()