class Appliance:
    def operate(self):
        pass


class WashingMachine(Appliance):
    def operate(self):
        print("WashingMachine is washing clothes.")
class Refrigerator(Appliance):
    def operate(self):
        print("Refrigerator is keeping our food cool.")

class Microwave(Appliance):
    def operate(self):
        print("Microwave is heating our food.")

w = WashingMachine()
r = Refrigerator()
m = Microwave()

for appliance in (w,r,m):
        appliance.operate()


