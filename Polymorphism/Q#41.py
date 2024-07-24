class Employee:
    def __init__(self,name):
        self.name = name
    def work(self):
        print("Child class implement this methof")
class Manager(Employee):
    def __init__(self,name):
        self.name = name
    def work(self):
        print(f"{self.name} is Manager")
class Developer(Employee):
    def __init__(self,name):
        self.name = name
    def work(self):
        print(f"{self.name} is wordpress Developer")
class Designer(Employee):
    def __init__(self,name):
        self.name = name
    def work(self):
        print(f"{self.name} is Graphic Designer")

m = Manager("Hassan")
d = Developer("Ali")
s = Designer("Asif")
for x in (m,d,s):
 x.work()