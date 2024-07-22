class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width

    def area(self):
        calculate_area=self.length*self.width
        print(f"Area is: {calculate_area}")

    def perimeter(self):
        calculate_perimeter=(self.length+self.width)*2
        print(f"Perimeter : {calculate_perimeter}")

obj=Rectangle(3,4)
obj.area()
obj.perimeter()
