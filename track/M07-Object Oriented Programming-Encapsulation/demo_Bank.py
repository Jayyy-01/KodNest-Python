class Bank:
    def __init__(self,balance):
        self.balance = balance
    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
    def withdraw(self,amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
    def display(self):
        return self.balance


account = Bank(10000)                    #total balance
print(account.display())

account.deposit(5000)           #adding 5000 rupees to account
print(account.display())

account.withdraw(2000)          #withdrawing 2000 rupees from account
print(account.display())

account.withdraw(3000)          #withdrawing 3000 rupees from account
print(account.display())        #displaying the amount present in account


#summary of the code is : we created a bank class with deposit,withdraw and display methods. 
#we created an account object with initial balance of 10,000 rupees.
#we then deposited 5,000 rupees to the account and displayed the total amount present in account.
#finally we withdrew 2,000 rupees and 3,000 rupees from the account and displayed the total amount present in account.
