class Employee:
    def __init__(self, name):
        self.name = name
        print("Employee Constructor")

class Developer(Employee):
    def __init__(self,name):
        print("Developer Constructor started")
        super().__init__(name)      #calling parent class constructor using super() method
        print("Developer Constructor completed")
        print(f"Developer: {self.name}")

name = input().strip()

dev = Developer(name)


#summary is we are creating obj for child class and we are inheriting constructor from parent class
#in this constructor overriding we are calling constructor of parent class from child class using super() method
#so it will print both parent constructor and child constructor
#this is recommended way to inherit constructor from parent class
#this is single inheritance we are inheriting only one parent class