class Employee:
    companyName = "KodNest"     #class variable 

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def printDetails(self):
        print(Employee.companyName)     #companyName is class variable and it is accessed through class name, Employee i.e(Employee.companyName)
        print(self.id)                      

e1 = Employee(1,"jay")
e2 = Employee(2,"tej")
print("First employee details : ") 
e1.printDetails()
print("Second employee details : ")
e2.printDetails()     



#class variable can be accessed through reference variable too i.e (e1.companyName) but it is not recommended
#if we change company name in one object it will not change for other objects