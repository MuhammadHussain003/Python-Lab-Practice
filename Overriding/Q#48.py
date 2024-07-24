class Vehicle:
    def __init__(self,name):
        self.name = name
    def fuel_efficiency(self):
        pass
class Car(Vehicle):
    def __init__(self,name,no_of_km_travel,no_of_fuel_consume):
        super().__init__(name)
        self.no_of_km_travel = no_of_km_travel
        self.no_of_fuel_consume = no_of_fuel_consume
    def fuel_efficiency(self):
        fuel_consumption = self.no_of_km_travel/self.no_of_fuel_consume
        print(f"{self.name} consume {fuel_consumption} litre after  per 1 Km")

class MotorBike(Vehicle):
    def __init__(self,name,no_of_km_travel,no_of_fuel_consume):
        super().__init__(name)
        self.no_of_km_travel =no_of_km_travel
        self.no_of_fuel_consume = no_of_fuel_consume
    def fuel_efficiency(self):
        fuel_consumption = self.no_of_km_travel / self.no_of_fuel_consume
        print(f"{self.name} consume {fuel_consumption} litre after  per 1 Km")

c = Car("Honda civic",300,3)
c.fuel_efficiency()
b = MotorBike("Honda 70",100,2)
b.fuel_efficiency()