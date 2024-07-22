class Animal:
    def __init__(self,name):
        self.name = name
    def eat(self):
        print(f"{self.name} is eating")

class Mammal(Animal):
    def __init__(self , name,color):
        super().__init__(name)
        self.color=color
    def nurse(self):
        print(f"{self.name} is nursing....")
class Dog(Mammal):
    def __init__(self,name,color,breed):
        super().__init__(name,color)
        self.breed=breed

    def bark(self):
        print(f"{self.name} is barking")


d=Dog("ullu","Black & white","Husky")
d.nurse()
d.bark()
print(d.color)
m=Mammal("fog","black")
m.nurse()