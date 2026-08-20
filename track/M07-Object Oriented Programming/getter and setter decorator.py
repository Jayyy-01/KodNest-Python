#here we are getting and updating(setting) values using direct attributes rather than calling methods
class Student:
    def __init__(self,roll,name):
        self.__roll = roll
        self.__name = name
    
    @property
    def roll(self):             #same as getter method but by using decorator
        return self.__roll
    
    @property
    def name(self):             #same as getter method but by using decorator
        return self.__name

    @roll.setter            #here we need to write the same variable which is used for updating i.e line 27(s1.roll) so whenever that is updating it will call this particular method
    def roll(self,roll):        #same as setter method but by using decorator
        self.__roll = roll  
    
    @name.setter            #similarly it will call this particular method whenever line 28 is updating
    def name(self,name):        #same as setter method but by using decorator
        self.__name = name

s1 = Student(11,"jay")
print(s1.roll)           #it is accessing the data of __roll (which is private variable)
print(s1.name)           #it is accessing the data of __name (which is private variable)

s1.roll = 100            #it is updating the the roll value
s1.name = "jayasree"     #it is updating the the name value

print(s1.roll)           #it is accessing the updated roll value
print(s1.name)           #it is accessing the updated name value

#here we are accessing and updating private variables using direct attributes rather than calling methods
#using this we can make data private and can access and update through direct attributes
#in this case it is same as using getter and setter methods but it is in the form of decorators
#