# Online Food Ordering System
# Features:
# Add food items to menu
# Place order
# Generate bill
# Cancel order
# View order history

class FoodItem:
    def __init__(self, name, price):
        self.name = name
        self.__price = price   # private variable (Encapsulation)

    def get_price(self):
        return self.__price

    def display(self):
        print(self.name, "- Rs.", self.__price)

class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def generate_bill(self):
        if len(self.items) == 0:
            print("No items in order!")
            return 0
        total = 0
        print("\nYour Order:")
        for item in self.items:
            item.display()
            total += item.get_price()
        print("Total Bill =", total)
        return total
    
    def cancel_order(self):
        self.items.clear()
        print("Order Cancelled!")

class Payment:
    def pay(self, amount):
        print("Payment Done")

class UPI(Payment):
    def pay(self, amount):
        print("Paid Rs.", amount, "using UPI")
        print("Thank You for ordering! Enjoy your meal.")   

class Cash(Payment):
    def pay(self, amount):
        print("Paid Rs.", amount, "using Cash")
        print("Thank You for ordering! Enjoy your meal.")   

menu = []      # initially empty menu
order = Order()
while True:
    print("\n------ONLINE FOOD ORDERING SYSTEM------")
    print("1. Add Food Item")
    print("2. Show Menu")
    print("3. Place Order")
    print("4. Generate Bill")
    print("5. Cancel Order")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter food name: ")
        price = int(input("Enter price: "))
        item = FoodItem(name, price)
        menu.append(item)
        print("Food Item Added!")

    elif choice == 2:
        if len(menu) == 0:
            print("Menu is Empty!")
        else:
            print("\nMenu:")
            for i in range(len(menu)):
                print(i+1, end=". ")
                menu[i].display()
    
    elif choice == 3:
        if len(menu) == 0:
            print("Menu is Empty!")
        else:
            print("\nSelect Item:")
            for i in range(len(menu)):
                print(i+1, end=". ")
                menu[i].display()

            item_no = int(input("Enter item number: "))
            order.add_item(menu[item_no-1])
            print("Item Added to Order!")

    elif choice == 4:
        amount = order.generate_bill()
        if amount > 0:
            print("1. UPI")
            print("2. Cash")
            p = int(input("Choose payment method: "))
            if p == 1:
                payment = UPI()
            else:
                payment = Cash()
            payment.pay(amount)

    elif choice == 5:
        order.cancel_order() 

    else:
        print("Exiting....")
        break