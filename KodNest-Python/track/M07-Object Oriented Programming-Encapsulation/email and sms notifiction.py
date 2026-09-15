class Notification:
    def send(self, message):
        return f"Message: {message}"


class EmailNotification(Notification):
    def send(self, message):
        # Reuse the parent method and add the email channel
        return f"{super().send(message)} | Sent by Email"       #calling parent class send method using super


class SMSNotification(Notification):
    def send(self, message):
        # Reuse the parent method and add the SMS channel
        return f"{super().send(message)} | Sent by SMS"        #calling parent class send method using super


message = input()     #taking the input from the user

email = EmailNotification()     #creating the object of EmailNotification class
sms = SMSNotification()

print(email.send(message))      #calling send method of EmailNotification class
print(sms.send(message))      #calling send method of SMSNotification class

#summary : here i created class Notification and _init_ method and i used it to create one object and display the object using print(job)
# and also used it to send message
# and in EmailNotification class i created send method and i used it to send the message
# and in SMSNotification class i created send method and i used it to send the message