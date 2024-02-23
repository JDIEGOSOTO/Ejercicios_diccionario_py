class GestionEmpleados():
    def __init__(self):
        self.employees = {}

    def add_employee(self):
        employee_id = str(len(self.employees) + 1)
        nombre = input("Type the name of the employee: ")
        posicion = input("Type the position of the employee: ")
        salario = float(input("Type the salary of the employee: "))
        self.employees[employee_id] = { "name" : nombre, "position" : posicion, "salario" : salario}

    def delete_employee(self):
        self.show_employees()
        employee_id = input("Type the ID of the employee you want to remove: ")
        if employee_id in self.employees:
            del self.employees[employee_id]
            print("Employee eliminated.")
        else:
            print("Employee not found")

    def update_employee(self):
        self.show_employees()
        employee_id = input("Type the ID of the employee you want to remove: ")
        if employee_id in self.employees:
            option = input("Select what you want to update: ")
            print("1.- Name")
            print("2.- Position")
            print("3.- Salary")
            if option == "1":
                new_name = input("Type the new name: ")
                self.employees[employee_id]["name"] = new_name
                print("Updated!")
            elif option == "2":
                new_position = input("Type the new position: ")
                self.employees[employee_id]["position"] = new_position
                print("Updated!")
            elif option == "3":
                new_salary = input("Type the new name: ")
                self.employees[employee_id]["salario"] = new_salary
                print("Updated!")
            else:
                print("Invalid option")
        else:
            print("Invalid option")


    def show_employees(self):
        print("List of employees: ")
        for id, employee in self.employees.items():
            print(f"Employee {id}: ")
            employee_info = f"Name: {employee["name"].title()}, Position: {employee["position"].title()}, Salario: {employee["salario"]}"
            print(employee_info)

gestion1 = GestionEmpleados()
gestion1.add_employee()
gestion1.show_employees()
gestion1.update_employee()
gestion1.show_employees()