class Employee:
    def __init__(self, name):
        self.name = name

class Developer(Employee):
    def __init__(self,name,language):
        super().__init__(name)  #it will call parent class constructor using super() method and it is taking name as an argument from child class to the parent class constructor
        self.language = language
    
    def display_profile(self):
        print(f"Name: {self.name}")
        print(f"Language: {self.language}")

name = input().strip()
language = input().strip()

dev = Developer(name,language)        #here dev is reference variable and we are calling Child class object
dev.display_profile()                   #here display_profile() method of Child class which is Child class 


#summary is 
#we can achieve this in two ways:-
#1. we can create object for parent class and access parent class constructor or parent class methods
#2. we can use super() method to call parent class constructor or parent class methods from child class    