class Student:
    def __init__(self,roll,name):
        if roll > 0:        #encapsulation of data i.e making it private
            self.__roll = roll
        else:
            self.__roll = None      #because if roll is < 0, it never creates instance of roll
            print("Invalid roll number")
        self.__name = name
    def setRoll(self,roll):      #encapsulation of data
        self.__roll = roll
    def getRoll(self):
        return self.__roll
    def setName(self,name):
        self.__name = name
    def getName(self):
        return self.__name

s1 = Student(11, "Jay")
# print(s1.__roll)          #cannot access the private variable directly through attributes
# print(s1.__name)
print(s1.getRoll())       #accessing through getter method
print(s1.getName())       #accessing through getter method

s1.setRoll(12)      #updating the roll value using setter method
s1.setName("Tej")   #updating the name value using setter method
# print(s1.__roll)
# print(s1.__name)
print(s1.getRoll())       #accessing through getter method
print(s1.getName())       #accessing through getter method


#summary is we can access private variables through getter and update the values through setter method
#using getter and setter we can make data private
#when we make a variable private, we cannot access directly through attributes, though we give __ (eg: print(s1.__name)), it raises error
