class Student:
    def __init__(self,roll,name):
        self.__roll = roll
        self.__name = name
    
    @property
    def roll(self):
        return self.__roll
    
    @property
    def name(self):
        return self.__name 
    
s1 = Student(12,"jay") 
print(s1.roll)
print(s1.name)


#here we are accessing data of roll and name using direct attributes(through @property, which is same syntax as getter)
#usually private attributes are not accessed directly, but through getter and setter methods it is possible
#here we are accessing using @property which is a decorator, using this we can access the private variables directly