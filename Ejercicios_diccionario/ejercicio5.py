class PhoneBook():
    def __init__(self):
        self.phones = {}
        self.numbers = {}

    def add_phone(self):
        key = input("Type the name of the contact: ")
        value = input(f"Type the {str(key).title()} phone number: ")
        self.phones[key] = value
        print(f"{key.title()} ({self.phones[key]}) has been added succesfully!")
    
    def modify_contacts(self):
        self.show_phonebook()
        search = input("Type the name of the contact you want to modify: ")
        if search in self.phones.keys():
            option = input("Type 'n' to modify the contact name, or type 'p' to modify the phone number: ")
            if option == "n":
                new_key = input("Type the new contact name: ")
                value = self.phones.pop(search)
                self.phones[new_key] = value
                print(f"{search.title()} is now called: {new_key.title()}")
            elif option == "p":
                new_value = input("Type the new phone number: ")
                old_key = search
                self.phones.pop(search)
                self.phones[old_key] = new_value
                print(f"{str(self.phones[old_key])} is the new number for {search.title()}")
            else:
                print("Not a valid option.")
        else:
            print("Contact not found")

    def delete_contact(self):
        self.show_phonebook()
        search = input("Type the name of the contact you want to delete: ")
        if search in self.phones.keys():
            self.phones.pop(search)
            print(f"{search.title()} has been eliminated.")
        else:
            print("Contact not found.")

    def show_phonebook(self):
        print("List of contacts")
        for k, v in self.phones.items():
            print(f"{k} : {v}")


        

contact1 = PhoneBook()

contact1.add_phone()
contact1.modify_contacts()
contact1.show_phonebook()
contact1.delete_contact()
contact1.show_phonebook()

