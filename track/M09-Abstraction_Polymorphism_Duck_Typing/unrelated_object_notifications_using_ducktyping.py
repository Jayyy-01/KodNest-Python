class EmailNotification:
    def __init__(self, message):
        self.message = message

    def send(self):
        return "Email: " + self.message


class SMSNotification:
    def __init__(self, message):
        self.message = message

    def send(self):
        return "SMS: " + self.message


class PushNotification:
    def __init__(self, message):
        self.message = message

    def send(self):
        return "Push: " + self.message


def send_notifications(notifications):
    for notification in notifications:      # iterating through the list of notifications objects
        result = notification.send()        # calling the send method from the objects and send() is not defined in Notification class but it is defined in the child classes because ducktyping is used here
        print(result)                       # printing the result


message = input()                           # getting the message from the user

notifications = []                                  # list of notifications objects                                        
notifications.append(EmailNotification(message))      # appending email notification object                                
notifications.append(SMSNotification(message))      # appending sms notification object
notifications.append(PushNotification(message))     # appending push notification object

send_notifications(notifications)