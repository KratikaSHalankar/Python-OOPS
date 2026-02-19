class BankAccount:
    
    def __init__(self,account_number,balance):
        self.__account_number = account_number # PRIVATE ATTRIBUTES
        self.__balance = balance # PRIVATE ATTRIBUTES

    
    def check_balance(self):
        print(f"Current Balance is {self.__balance}")
        
    
    def deposit(self,amount):
        self.__balance = self.__balance  + amount
        print(f"Deposited {amount} successfully!")
    
    def withdraw_funds(self,amount):
        if amount < self.__balance:
            self.__balance = self.__balance - amount
            print(f" {amount} has been withdrawed successfully")
        else:
            print("Insufficent Balance")
    
acc = BankAccount(123456789,5000)
acc.check_balance()

acc.deposit(200)
acc.check_balance()

acc.withdraw_funds(1000)
acc.check_balance()


print(acc.balance) 
#AttributeError: 'BankAccount' object has no attribute 'balance' because we can access the private attributes only throught the methods which are inside in the class