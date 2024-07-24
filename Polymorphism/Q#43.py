class Animal:
    def __init__(self,sound):
        self.sound = sound
    def speak(self):
        pass
class Dog(Animal):
    def __init__(self,sound):
        self.sound = sound
    def speak(self):
        print(f"""
               Dog sound like : {self.sound}
""")
class Cat(Animal):
    def __init__(self,sound):
        super().__init__(sound)

    def speak(self):
        print(f"""
                 Cat sound like: {self.sound}
                 """)
class Cow(Animal):
    def __init__(self,sound):
        super().__init__(sound)
        self.sound = sound
    def speak(self):
        print(f"""
               Cow  sound like : {self.sound}
                 """)

d = Dog("woof")
c = Cat("Meows")
cow = Cow("Mooo")
for x in (d,c,cow):
    x.speak()