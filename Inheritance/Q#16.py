class Shape:
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


class Triangle(Shape):
    def __init__(self, base, hypotenus):
        self.base = base
        self.hypotenus=hypotenus

    def calculate_area(self):
        print("Area of Triangle : ", 1/2*self.base * self.hypotenus)

c = Circle(3)
c.calculate_area()

r = Rectangle(5,6)
r.calculate_area()

t = Triangle(4,5)
t.calculate_area()





