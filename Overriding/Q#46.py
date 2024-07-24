class Animal:
    def move(self):
        pass
class Bird(Animal):
    def move(self):
        print("Birds are flying in air")
class Fish(Animal):
    def move(self):
        print("Fish are swimming in water")
class Mammal(Animal):
    def move(self):
        print("Mammal are walk on land")


b = Bird()
b.move()
f = Fish()
f.move()
m = Mammal()
m.move()