# Student Report Card Generator :
# Build a system that collects student data and subject-wise marks to generate a report card.
# Include grade calculation, average score, and pass/fail result.
# Use encapsulation for mark storage and method abstraction for result generation.
# These challenges progressively test the understanding of core OOP principles like 
# inheritance, polymorphism, abstraction, and encapsulation, while also encouraging real-world problem-solving.

# Parent Class
class Student:

    def __init__(self, usn, name):
        self.usn = usn
        self.name = name
        self.__marks = []   # Encapsulation (Private Data)

    def add_marks(self, mark):
        self.__marks.append(mark)

    def calculate_average(self):
        if len(self.__marks) == 0:
            return 0
        total = sum(self.__marks)
        avg = total / len(self.__marks)
        return avg

    # Method to check result (Abstraction)
    def result(self):
        avg = self.calculate_average()
        if avg >= 40:
            return "PASS"
        else:
            return "FAIL"

    def display_report(self):
        print("\n------ REPORT CARD ------")
        print("USN:", self.usn)
        print("Name:", self.name)
        print("Marks:", self.__marks)
        print("Average:", self.calculate_average())
        print("Grade:", self.calculate_grade())  # Polymorphism
        print("Result:", self.result())


# UG Student Class(Inheritance)
class UGStudent(Student): #child class

    # Method Overriding (Polymorphism)
    def calculate_grade(self):
        avg = self.calculate_average()
        if avg >= 90:
            return "A"
        elif avg >= 75:
            return "B"
        elif avg >= 50:
            return "C"
        else:
            return "F"


# PG Student Class (Inheritance)
class PGStudent(Student): #child class

    # Method Overriding(Polymorphism)
    def calculate_grade(self):
        avg = self.calculate_average()
        if avg >= 85:     
            return "A"
        elif avg >= 70:
            return "B"
        elif avg >= 50:
            return "C"
        else:
            return "F"


student = None

while True:
    print("\n1. Create UG Student")
    print("2. Create PG Student")
    print("3. Add Marks")
    print("4. Display Report Card")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        usn = input("Enter USN: ")
        name = input("Enter Name: ")
        student = UGStudent(usn, name)
        print("UG Student Created!")

    elif choice == 2:
        usn = input("Enter USN: ")
        name = input("Enter Name: ")
        student = PGStudent(usn, name)
        print("PG Student Created!")

    elif choice == 3:
        if student:
            mark = float(input("Enter Marks: "))
            student.add_marks(mark)
            print("Marks Added!")
        else:
            print("Create student first!")

    elif choice == 4:
        if student:
            student.display_report()
        else:
            print("No Student Found!")

    elif choice == 5:
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")