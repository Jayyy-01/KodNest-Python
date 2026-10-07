from abc import ABC,abstractmethod
class PaymentProcessor(ABC):
   @abstractmethod
   def process_payment(self):
       pass

class UPIPayment(PaymentProcessor):
    def __init__(self, amount):
        self.amount = amount

    def process_payment(self):
        return f"UPI Payment: {self.amount}"

class CardPayment(PaymentProcessor):
    def __init__(self, amount):
        self.amount = amount

    def process_payment(self):
        return f"Card Payment: {self.amount}"
            
class NetBankingPayment(PaymentProcessor):
    def __init__(self, amount):
        self.amount = amount

    def process_payment(self):
        return f"Net Banking Payment: {self.amount}"

upi_amount = int(input())
card_amount = int(input())
net_banking_amount = int(input())

upi = UPIPayment(upi_amount)
card = CardPayment(card_amount)
net_banking = NetBankingPayment(net_banking_amount)

payment = [upi,card,net_banking]

for i in payment:
    print(i.process_payment())



