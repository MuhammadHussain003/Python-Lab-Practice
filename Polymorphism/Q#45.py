class Vehicle:
    def start(self):
        pass
class Car(Vehicle):
    def start(self):
        print("Car is start by rotating key ")
class Bike(Vehicle):
    def start(self):
        print("Bike is start by kicking")
class Boat(Vehicle):
    def start(self):
        print("Boat is start by pulling the rope ")




c = Car()
b = Bike()
b2 = Boat()

for call in (c,b,b2):
    call.start()
