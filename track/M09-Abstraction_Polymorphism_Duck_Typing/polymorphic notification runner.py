from abc import ABC, abstractmethod


class NotificationService(ABC):
    def __init__(self, message):
        self.message = message

    @abstractmethod
    def notify(self):
        pass


class EmailNotificationService(NotificationService):
    def __init__(self, message):
        self.message = message

    def notify(self):
        return "Email: " + self.message


class SMSNotificationService(NotificationService):
    def __init__(self, message):
        self.message = message

    def notify(self):
        return "SMS: " + self.message


def run_notifications(services):
    for service in services:
        result = service.notify()
        print(result)


message = input()

services = []
services.append(EmailNotificationService(message))
services.append(SMSNotificationService(message))

run_notifications(services)

# duck typing example
# if the object has the method 'notify' then it is a NotificationService and it works
# the 'notify' method in both the classes are doing different things
# this is a good example of polymorphism and abstraction
# there are two child classes EmailNotificationService and SMSNotificationService which are derived from the abstract class NotificationService
# the output is the notification in two seperate lines