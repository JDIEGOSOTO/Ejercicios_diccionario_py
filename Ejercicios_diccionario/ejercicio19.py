class VehicleRental():
    def __init__(self):
        self.vehicles = {}
    
    def add_vehicle(self):
        vehicle_id = str(len(self.vehicles) + 1)
        name = input("Type the name of the vehicle: ")
        brand = input("Type the brand of the vehicle: ")
        cost = input("Cost of renting: ")
        availability = input("Is this vehicle available for renting?(yes/no)")
        if availability == "yes":
            self.vehicles[vehicle_id] = { "name" : name, "brand" : brand, "cost": cost, "availability" : "available" }
        elif availability == "no":
            self.vehicles[vehicle_id] = { "name" : name, "brand" : brand, "cost": cost, "availability" : "not available" }

    def show_vehicles(self):
        print("Lis of Vehicles: ")
        for id, vehicle in self.vehicles.items():
            print(f"Vehicle {id}: ")
            vehicle_info = f"Name: {vehicle["name"].title()}, Brand: {vehicle["brand"].title()}, Cost: {vehicle["cost"]}, Availability: {vehicle["availability"].title()} "
            print(vehicle_info)


rent1 = VehicleRental()
rent1.add_vehicle()
rent1.show_vehicles()