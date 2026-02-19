def menu():
    print("\nWelcome to Banking System")
    print("This System provides the following services: ")
    print("1.Check Balance")
    print("2.Deposit ")
    print("3.Withdraw ")
    print("4.Exit")

    
balance = 100
while(True):
    menu()
    choice = int(input("Enter the service you want: "))
    if choice == 1:
        print(f"Balance in the account is: {balance}")

    elif choice == 2:
        amount = int(input("Enter the amount to Deposit: "))
        balance = balance + amount

    elif choice == 3:
        amount = int(input("Enter the amount to withdraw: "))
        if balance <= amount:
            print("Insufficient balanace!")
        else:
            balance = balance - amount
            print(f"{amount} has been withdrawn successfully! ")

    else:
        print("Thank you for Visiting!")
        break

