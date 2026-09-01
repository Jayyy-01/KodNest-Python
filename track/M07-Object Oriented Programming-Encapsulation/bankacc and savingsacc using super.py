class BankAccount:
    def __init__(self, account_holder):
        self.account_holder = account_holder

    def show_holder(self):
        return f"Account Holder: {self.account_holder}"


class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance):
        # Call the parent constructor
        super().__init__(account_holder)
        # Store balance
        self.balance = balance

    def show_balance(self):
        # Return the balance
        return f"Balance: {self.balance}"


name = input()  
balance = int(input())   

account = SavingsAccount(name, balance)    

print(account.show_holder())     #calling show_holder method from BankAccount class
print(account.show_balance())     #calling show_balance method from SavingsAccount class

#summary : here i created class BankAccount and _init_ method and i used it to create one object and display the object using print(job)
# and also used it to show account holder
# and in SavingsAccount class i created show_balance method and i used it to show the balance