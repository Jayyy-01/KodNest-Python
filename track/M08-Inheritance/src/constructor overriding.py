class Parent:
    def __init__(self):
        print("Parent Constructor")

class Child(Parent):
    def __init__(self):
        print("Child constructor")

ch = Child()

#summary is we are creating obj for child class and we are overriding constructor of parent class because constructor name is same for both parent and child class
#in this constructor overriding we are not calling constructor of parent class from child class using super() method
#so it will only print child constructor not parent constructor
#as it is happening for constructor, it is called as constructor overriding
#as we are not calling constructor of parent class from child class using super() method, it is not recommended way to inherit constructor from parent class
#to inherit constructor from parent class we should use super() method
