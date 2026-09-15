class objectCount:
    count = 0       #class variable
    def __init__(self,roll):
        self.roll = roll    
        objectCount.count += 1  #accessing the class variable using class name i.e objectCount and incrementing count by 1

o1 = objectCount(101)
o2 = objectCount(102)
o3 = objectCount(103)
o4 = objectCount(104)
o5 = objectCount(105)
print(f"Total number of objects = {objectCount.count}")


#whenever we create an object, __init__() will get called and the count will get incremented by 1 for each object