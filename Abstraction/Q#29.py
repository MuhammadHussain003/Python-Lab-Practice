from abc import ABC,abstractmethod
class Vehicle(ABC):
    def __init__(self,name):
        self.name=name
    def vehicle(self):
        print("Every vehicle need petrol to run")
    @abstractmethod
    def start_engine(self):
        pass
class Car(Vehicle):
     def __init__(self,name):
         super().__init__(name)

     def start_engine(self,):
         print("Car engine is start by rotating the key ")

class Motorcycle(Vehicle):
    def __init__(self,name):
        super().__init__(name)
    def start_engine(self):
        print("Motor cycle engine is start by kick start")

c = Car("Civic")
c.start_engine()
b = Motorcycle("Honda 70")
b.start_engine()