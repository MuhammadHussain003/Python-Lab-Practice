from abc import ABC,abstractmethod
class Appliance(ABC):
    def __init__(self,company):
        self.company = company
    def appliance(self):
        print("Every device that need electricity to start.....")

    @abstractmethod
    def turn_on(self):
        pass
class WashingMachine(Appliance):
    def __init__(self,company):
        super().__init__(company)
    def turn_on(self):
        print(f"{self.company} : Washing machine ")
class Refrigerator(Appliance):
    def __init__(self,company):
        self.company = company
    def turn_on(self):
        print(f" {self.company} : Refrigerator ")

class Oven(Appliance):
    def __init__(self,company):
        self.company = company
    def turn_on(self):
        print(f" {self.company} : Oven ")

w = WashingMachine("Dawlance")
w.turn_on()
o = Oven("National")
o.turn_on()