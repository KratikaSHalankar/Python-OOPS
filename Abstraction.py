from abc import ABC, abstractmethod

class ATM(ABC):

    def start(self):
        print("Insert the card")
        self.lang = input("Select language [eng/kan/hindi]: ")
        self.acc_type = input("Account type [Savings/Current/Fixed]: ")
        self.pin = int(input("Enter 4-digit PIN: "))
        self.amount = int(input("Enter amount to withdraw: "))

        self.withdraw(self.amount)

    @abstractmethod
    def withdraw(self, amount):
        pass
class CanaraBank(ATM):
    def withdraw(self, amount):
        print(f"Debited {amount} Rs from your Canara Bank account")
        print("Transaction successful. Collect cash 💵")
class SBIBank(ATM):
    def withdraw(self,amount):
        print(f"Debited {amount} Rs from your SBI account")
        print("Transaction successful. Collect cash 💵")


user1 = CanaraBank()
user1.start()