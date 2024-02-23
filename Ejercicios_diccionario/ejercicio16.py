class ProyectManager():
    def __init__(self):
        self.proyects = {}

    def add_proyect(self):
        proyect_id = str(len(self.proyects) + 1)
        nombre = input("Type the name of the proyect: ")
        owner = input("Type the owner of the proyect: ")
        type = input("Enter the type of the proyect: ")
        self.proyects[proyect_id] = { "name" : nombre, "owner" : owner, "type" : type }

    def show_proyects(self):
        print("Lis of Proyects: ")
        for id, proyect in self.proyects.items():
            print(f"Proyect {id}: ")
            proyect_info = f"Name: {proyect["name"].title()}, Owner: {proyect["owner"].title()}, Type: {proyect["type"].title()}"
            print(proyect_info)

proyect1 = ProyectManager()
proyect1.add_proyect()
proyect1.show_proyects()