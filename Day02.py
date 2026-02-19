class Employee:
    def __init__(self, name, designation, salary = 30000):# salary is a optional parameter
        self.name = name
        self.designation = designation
        self.salary = salary

    def show(self):
        print(f"{self.name} is working in {self.designation} with salary of {self.salary} ")

e1 = Employee("Rahul", 'HR', '80000') # user has set value
e2 = Employee("Priya" , 'Maneger') # uses the default value

e1.show()
e2.show()