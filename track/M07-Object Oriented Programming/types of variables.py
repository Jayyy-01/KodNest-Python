a = 100         #global variable
class Employee:
    def __init__(self, id, name):       #id and name are local variables
        self.id = id            #self.id is instance variable
        self.name = name        #self.name is instance variable

e1 = Employee(11,"jay")         #e1 is reference variable
print(e1.id)                    #accessing instance variable through object
print(e1.name)                  #accessing instance variable through object
print(a)                        #accessing global variable


#instance variables are different for each object
#global variables are same for all objects