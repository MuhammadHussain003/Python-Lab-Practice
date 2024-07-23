from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name):
        self.name = name
    def animal(self):
        print("Every animal has a different sound")

    @abstractmethod
    def make_sound(self):
        pass


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
    def make_sound(self):
        print("Dog sound is woof")



class Cat(Animal):
    def __init__(self,name):
        super().__init__(name)
    def make_sound(self):
        print("Cat sound is meows")

class Bird(Animal):
    def __init__(self, name):
        super().__init__(name)
    def make_sound(self):
         print(" chirping")

d=Dog("Husky")
d.make_sound()
c = Cat("Billi")
c.make_sound()

