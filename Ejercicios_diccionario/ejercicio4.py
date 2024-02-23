class Inventory():
    def __init__(self):
        self.inventory = {}
        self.product = {}
    
    def add_product(self):
        product_id = len(self.inventory) + 1
        nombre = input("Type the name of the product: ")
        self.product["name"] = nombre
        cantidad = int(input("Type the amount of the product: "))
        self.product["amount"] = cantidad
        precio = float(input("Type the price of the product: "))
        self.product["price"] = precio

        self.inventory[product_id] = self.product["name"], self.product["amount"], self.product["price"]

    def show_inventory(self):
        for k, v in self.inventory.items():
            print(f"{k} : {v}")

product1 = Inventory()

product1.add_product()
product1.show_inventory()