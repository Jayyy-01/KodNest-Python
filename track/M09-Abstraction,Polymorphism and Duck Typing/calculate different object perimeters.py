class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def perimeter(self):
        return 2 * (self.length + self.width)

class Square:
    def __init__(self,side):
        self.side = side
    def perimeter(self):
        return 4 *(self.side)

length = int(input())
breadth = int(input())
side = int(input())
rectangle = Rectangle(length,breadth)
square = Square(side)

shape = [rectangle,square]
for i in shape:
    print(i.perimeter())

#summary : here i created two classes rectangle and square and i created perimeter method in both classes and i used it to calculate the perimeter of rectangle and square and display the result