# This Inventory Management System simulates 
# how a real shopkeeper manages stock items such as groceries and electronics.
# It helps in adding, updating, searching and calculating the total value of items present in the shop inventory.

class Item: #parent class
    def __init__(self, name, price, quantity):
        self.name = name
        self.__price = price #private:Encapsulation
        self.__quantity = quantity #private:Encapsulation

    def get_price(self):
        return self.__price
    
    def get_quantity(self):
        return self.__quantity
    
    def set_quantity(self, quantity):
        self.__quantity = quantity

    def cal_value(self):
        return self.__price * self.__quantity

#child class 1
class groceryItems(Item):
    def __init__(self, name, price, quantity, expiry):
        super().__init__(name, price, quantity) # super() to call the parent constructor
        self.expiry = expiry

    def cal_value(self): # same method but different behaviour(polymorphism)
        value= super().cal_value() #super() to call parent class method
        return value*0.9 #giving 10% discount on groceryitems

# child class 2
class ElectronicItems(Item):
    def __init__(self, name, price, quantity, warranty):
        super().__init__(name, price, quantity)
        self.warranty = warranty

    # Polymorphism (Method Overriding)
    def calculate_value(self):
        value = super().cal_value()
        return value * 1.18   # 18% GST for electronics
    
class Inventory:
    def __init__(self):
        self.items = []

    #to add grocery items
    def add_grocery(self, name, price, quantity, expiry):
        item = groceryItems(name, price, quantity, expiry)
        self.items.append(item)
        print("Grocery Item Added!")
    
    #to add electronic items
    def add_electronics(self, name, price, quantity, warranty):
        item = ElectronicItems(name, price, quantity, warranty)
        self.items.append(item)
        print("Electronic Item Added!")
    
    def display_items(self):
        if len(self.items) == 0:
            print("Inventory is Empty!")
            return

        for item in self.items:
            print("Name:", item.name)
            print("Price:", item.get_price())
            print("Quantity:", item.get_quantity())

    #updating the quantity
    def update_quantity(self, name, quantity):
        for item in self.items:
            if item.name == name:
                item.set_quantity(quantity)
                print("Quantity Updated Successfully!")
                return
        print("Item Not Found!")
    
    #to search a item
    def search_item(self, name):
        for item in self.items:
            if item.name == name:
                print("Item Found!")
                print("Name:", item.name)
                print("Price:", item.get_price())
                print("Quantity:", item.get_quantity())
                return
        print("Item Not Found!")

    #to calculate total stock available
    def total_value(self):
        total = 0
        for item in self.items:
            total += item.cal_value()
        print("Total Stock Value:", total)

inventory = Inventory()
while True:
    print("Welcome to Inventory Management System (IMS)")
    print("\n1.Add Grocery Item")
    print("2.Add Electronic Item")
    print("3.Display All Items")
    print("4.Update Item Quantity")
    print("5.Search Item")
    print("6.Total Stock Value")
    print("7.Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter Name: ")
        price = float(input("Enter Price: "))
        quantity = int(input("Enter Quantity: "))
        expiry = input("Enter Expiry Date: ")
        inventory.add_grocery(name, price, quantity, expiry)

    elif choice == 2:
        name = input("Enter Name: ")
        price = float(input("Enter Price: "))
        quantity = int(input("Enter Quantity: "))
        warranty = input("Enter Warranty: ")
        inventory.add_electronics(name, price, quantity, warranty)

    elif choice == 3:
        inventory.display_items()

    elif choice == 4:
        name = input("Enter Item Name: ")
        quantity = int(input("Enter New Quantity: "))
        inventory.update_quantity(name, quantity)

    elif choice == 5:
        name = input("Enter Item Name: ")
        inventory.search_item(name)

    elif choice == 6:
        inventory.total_value()

    elif choice == 7:
        print("Exisiting ")
        break

    else:
        print("Invalid Choice!")

    