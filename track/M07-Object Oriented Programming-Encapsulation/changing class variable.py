class Employee:
    companyName = "KodNest"     #class variable 

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def printDetails(self):
        print(Employee.companyName)     #companyName is class variable and it is accessed through class name, Employee i.e(Employee.companyName)
        print(self.id)                      
        print(self.name)                    

e1 = Employee(1,"jay")
e2 = Employee(2,"tej")
print("First employee details : ") 
e1.printDetails()
print("Second employee details : ")
e2.printDetails()     

Employee.companyName = "Wipro"     #changing class variable
print("First employee details : ") 
e1.printDetails()
print("Second employee details : ")
e2.printDetails()

