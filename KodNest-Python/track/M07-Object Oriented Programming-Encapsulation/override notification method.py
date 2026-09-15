class Notification:
    def send(self, message):
        print(f"General Notification: {message}")


class EmailNotification(Notification):      #here EmailNotification is a child class of Notification class
    # Override send()       #this method is used to override the send method of the parent class
    def send(self, message):
        print(f"Email Notification: {message}")


message = input().strip()       #taking the input from the user

# Create both objects and call send()
n = Notification()    #creating the object of Notification class 
e = EmailNotification()   #creating the object of EmailNotification class
n.send(message)   #calling the send method
e.send(message)   #calling the send method


#summary : here i created class Notification and _init_ method and i used it to create one object and display the object using print(job)
# i used send method in both classes and i used it to send the message  