class Shape:
    def __init__(self,name):
        self.name = name
    def draw(self):
        print("Child has implement this method")
class Circle(Shape):
    def __init__(self,name):
        super().__init__(name)
        self.name = name
    def draw(self):
        print(f"""
                Shape name : {self.name}
""")
class Rectangle(Shape):
    def __init__(self,name):
        super().__init__(name)
        self.name = name
    def draw(self):
        print(f"""
                 Shape Name : {self.name}
                 """)
class Triangle(Shape):
    def __init__(self,name):
        super().__init__(name)
        self.name = name
    def draw(self):
        print(f"""
                 Shape Name : {self.name}
                 """)

c = Circle("circle")
r = Rectangle( "Rectangle")
t = Triangle("Triangle")

for x in (c,r,t):
    x.draw()