class Parent:
    def __init__(self,name):
        self.name = name
        print("inside parent class")
    
class Child(Parent):
    def __init__(self,name,course):      #it will call parent class constructor using super() method and it is taking name as an argument from child class to the parent class constructor
        super().__init__(name)      #it will call parent class constructor using super() method and it is taking name as an argument from child class to the parent class constructor
        self.course = course
        print("inside child class")


ch = Child("jay","python")
print(ch.name)
print(ch.course)    