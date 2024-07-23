from abc import ABC, abstractmethod

class Drivable(ABC):
    @abstractmethod
    def drive(self):
        pass
class Car(Drivable):
    def drive(self):
        print("Driving car is comfortable and easy to drive.")
class Bike(Drivable):
    def drive(self):
        print("Driving bike is uncomfortable but easy as compare to car.")

class Truck(Drivable):
    def drive(self):
        print("Driving truck is comfortable but difficult to drive in thick road")


c =Car()
c.drive()

b = Bike()
b.drive()

t = Truck()
t.drive()