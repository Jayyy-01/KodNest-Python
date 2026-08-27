class Person:
    def display_name(self,name):
        print(f"Name: {name}")

class Student(Person):
    pass

name = input().strip()
# here i'm creating object for student class, but i'm calling display_name() method of Person class
# because Student class inherits all the methods of Person class
student = Student()     #here student is reference variable and we are calling Child class object
student.display_name(name)  #here display_name() method of Person class which is parent class