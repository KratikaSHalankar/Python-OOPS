class BankAccount:
    def __init__(self,balance):
        self.__balance = balance #private attribute
        
    def get_balance(self):
        print(f"The Balance is {self.__balance}")
        
    def set_balance(self,balance):
        if balance <=0:
            print("Balance cannot be zero ")
        else:
            self.__balance = balance
            print(f"The Balance is {self.__balance}")
            
b = BankAccount(10000)

b.get_balance() # to retrievethe balance      
b.set_balance(50000)  # updates the balance