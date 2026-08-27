class Student:
    def __init__(self,roll,name):
        self.roll = roll
        self.name = name
    def setRoll(self,roll):
        self.roll = roll
    def getRoll(self):
        return self.roll
    def setName(self,name):
        self.name = name
    def getName(self):
        return self.name

s1 = Student(11, "Jay")     #creating object
print(s1.roll)          #accessing the data using attribute
print(s1.name)          #accessing the data using attribute
print(s1.getRoll())     #accessing the data through getter method
print(s1.getName())     #accessing the data through getter method

s1.setRoll(12)          #updating roll using setter method
s1.setName("Tej")   #updating name using setter method
print(s1.roll)      #accessing the updated roll using attribute
print(s1.name)      #accessing the updated name using attribute
print(s1.getRoll()) #accessing the updated roll using getter method
print(s1.getName()) #accessing the updated name using getter method

#here we can access private variables through getter and update the values through setter method
#using getter and setter we can make data private
#when we make a variable private, we cannot access directly through attributes, though we give __ (eg: print(s1.__name)), it raises error