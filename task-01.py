# 1. Bank Account Management System
# Problem Statement: Design a menu-driven program that simulates a simple banking system. The program should allow the user to:
# 1.Create a new bank account
# 2.Deposit money
# 3.Withdraw money ( The system must prevent withdrawal if the balance is insufficient.)
# 4.Check account balance
# 5.Display account details
# 6.Exit

class Bank_Account:
    def __init__(self,account_number,account_name,balance=0.0):
        self.account_number = account_number
        self.account_name = account_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance = self.balance + amount
            print(f"{amount} deposited successfully! ")
        else:
            print("amount entered is Invalid. amount must be positive")

    def withdraw(self,amount):
        if amount > self.balance:
            print("Insufficient balance. Withdrawl denied! ")
        else:
            self.balance = self.balance - amount
            print(f"{amount} withdrawn successfully! ")

    def check_balance(self):
        print(f"current balance is {self.balance}")

    def display_details(self):
        print("\nACCOUNT DETAILES:")
        print(f"Account No. : {self.account_number}")
        print(f"Account Name. : {self.account_name}")
        print(f"Balance : {self.balance}")        
account = None
while True:
    print("\n--- Bank Menu ---")
    print("1. Create New Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. Display Account Details")
    print("6. Exit") 

    choice = int(input("Enter your choice: "))

    if choice == 1:
        if account is None:
            account_number = input("Enter Account Number: ")
            account_name = input("Enter Account Holder Name: ")
            balance = float(input("Enter Initial Balance: "))
            account = Bank_Account(account_number,account_name, balance)
            print("Account Created Successfully!")
        else:
            print("Account already Exists! ")   

    elif choice == 2:
        if account:
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        else:
            print("No account found. Please create an account first.")

    elif choice == 3:
        if account:
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        else:
            print("No account found. Please create an account first.")

    elif choice == 4:
        if account:
            account.check_balance()
        else:
            print("No account found. Please create an account first.")

    elif choice == 5:
        if account:
            account.display_details()
        else:
            print("No account found. Please create an account first.")

    elif choice == 6:
        print("Thank you for using the Bank Account Management System. Goodbye!")
        break
    
    else:
        print("Invalid choice. Please try again.")


