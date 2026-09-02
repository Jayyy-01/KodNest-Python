from abc import ABC, abstractmethod
class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self):      #abstract method
        pass

class UPIPayment(PaymentProcessor):
    def __init__(self, amount):    #init method
        self.amount = amount

    def process_payment(self):    #concreate method because it is defined in the class and it is not abstract method, also it is overridden from the abstract class and have body
        return f"UPI Amount: {self.amount}"

amount = int(input())

payment = UPIPayment(amount)
print(payment.process_payment())

#summary : here i created abstract class PaymentProcessor and i used it to create one object and display the object using print(payment.process_payment())


    
