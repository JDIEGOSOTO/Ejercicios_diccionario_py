class Heroe():
    def __init__(self):
        self.skills = {}

    def add_elements(self):
        key = input("Enter tbe name of the hability: ")
        value = input("Enter the value of the hability: ")
        self.skills[key] = value
        print("The hability " + key + " has been added.")

    def update_elements(self):
        print("List of habilities: ")
        for k in self.skills.keys():
            print(k)
        search = input("Enter the name of the hability : ")
        if search in self.skills.keys():
            option = input("Type 'k' to modify the name of the skill, or type 'v' to modify the content of the skill: ")
            if option == "k":
                new_key = input("Type the new name of the skill: ")
                value = self.skills.pop(search)
                self.skills[new_key] = value
            if option == "v":
                new_value = input("Type the new content of the skill: ")
                old_key = search
                self.skills.pop(search)
                self.skills[old_key] = new_value
            else:
                print("Not a valid option.")
        else: 
            print("Skill not found")

    def delete_elements(self):
        print("List of habilities: ")
        for k in self.skills.keys():
            print(k)
        search = input("Type the name of the skill you want to delete: ")
        if search in self.skills.keys():
            self.skills.pop(search)
            print(search + " has been eliminated.")
        else:
            print("Skill not found.")
        

    def show_elements(self):
        print(self.skills)

    

tusk = Heroe()
tusk.add_elements()
tusk.show_elements()
tusk.update_elements()
tusk.show_elements()
tusk.delete_elements()
tusk.show_elements()




    
