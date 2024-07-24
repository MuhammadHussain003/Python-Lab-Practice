class Shape:

    def calculate_area(self):
        pass
class Square(Shape):
    def __init__(self,side):
        self.side = side
    def calculate_area(self):
        print(f"Area of Square is : {self.side*4}")

class Triangle(Shape):
    def __init__(self,base,height):
        self.base = base
        self.height = height
    def calculate_area(self):
        print(f"Area of triangle is : {1/2*self.base*self.height}")

s = Square(4)
t = Triangle(4,6)
s.calculate_area()
t.calculate_area()
