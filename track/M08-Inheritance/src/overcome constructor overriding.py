class Employee:
    def __init__(self):
        print("Employee Constructor")

class Developer(Employee):
    def __init__(self):
        print("Developer Constructor started")
        super().__init__()      #calling parent class constructor using super() method
        print("Developer Constructor completed")

ch = Developer()

#we are creating object for child class and we are calling constructor of child class
#in this constructor overriding we are calling constructor of parent class from child class using super() method
#so it will print both parent constructor and child constructor
#this is recommended way to inherit constructor from parent class
#this is single inheritance we are inheriting only one parent class    

#summary is we can overcome constructor overriding by calling constructor of parent class from child class using super() method
#otherwise if we don't call constructor of parent class from child class using super() method, it is called as constructor overriding
#and it will not print parent constructor
#so it is recommended way to inherit constructor from parent class using super() method
#this is single inheritance we are inheriting only one parent class
