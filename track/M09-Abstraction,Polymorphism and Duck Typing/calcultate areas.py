class Rectangle:
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        return self.length * self.breadth
    
class Square:
    def __init__(self,side):
        self.side = side
    def area(self):
        return self.side * self.side

length = int(input())
breadth = int(input())
side = int(input())

shapes = [Rectangle(length,breadth),Square(side)]       # list contains two objects of Rectangle and Square classes and here both classes are having area method so it is called as polymorphism

for shape in shapes:        # for each shape in shapes list print the area method
    print(shape.area())   

#summary : here created two classes Rectangle and Square and __init__ and area method and used it to create one object and display the object using print(shape.area())   
#and both methods are having same name called area() only once, but it is behaving differently based on the object passed to the method, 
#so it is called as polymorphism