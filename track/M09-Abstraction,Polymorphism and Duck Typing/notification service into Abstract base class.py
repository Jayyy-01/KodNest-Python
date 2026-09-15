from abc import ABC, abstractmethod
class NotificationService(ABC):
    @abstractmethod
    def notify(self):
        pass

class EmailNotificationService(NotificationService):
    def __init__(self,message):
        self.message = message
    def send_email(self):
        return f"Email: {self.message}"
    def notify(self):
        return f"Email: {self.send_email()}"


class SMSNotificationService(NotificationService):
    def __init__(self,message):
        self.message = message
    def send_sms(self):
        return f"Sending SMS: {self.message}"
    def notify(self):
        return f"SMS: {self.send_sms()}"

message = input()

email = EmailNotificationService(message)
sms = SMSNotificationService(message)

print(email.notify())
print(sms.notify())