class Parent:
    def __init__(self, lastname):
        self.lastname = lastname

class Child(Parent):  # Inherit from Parent
    def __init__(self, lastname, firstname):
        super().__init__(lastname)  # Call Parent constructor
        self.firstname = firstname  # Correct attribute assignment
        
    def show(self):
        print(f"{self.firstname} {self.lastname}")  # Print full name

c = Child("Halankar", "Kratika")
c.show()