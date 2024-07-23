from abc import ABC,abstractmethod
class Shape(ABC):
    def shape(self):
        print("Every this has a specific Shape")
    @abstractmethod
    def calculate_area(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def calculate_area(self):
        pi=3.14
        print("Area of circle : ",pi*self.radius**2,"\n")

class Rectangle(Shape):
        def __init__(self,length,width):
            self.length = length
            self.width=width
        def calculate_area(self):
            print("Area of Rectangle : ", self.length*self.width,"\n")


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def calculate_area(self):
        print("Area of Square : ", self.side**4)

c = Circle(3)
c.calculate_area()

r = Rectangle(5,6)
r.calculate_area()

s= Square(4)
s.calculate_area()

