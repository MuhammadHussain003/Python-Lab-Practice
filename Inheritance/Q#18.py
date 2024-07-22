class Vehicle:
    def __init__(self,company,model):
        self.company=company
        self.model=model
    def detail(self):
        print(f"""
        {self.company}
        {self.model}  
""")


class Car(Vehicle):
    def __init__(self,company,model):
        super().__init__(company,model)

    def num_wheel(self):
        return 4
    def engine_type(self):
        return "Suzuki"

class Bike(Vehicle):
    def __init__(self,company,model):
        super().__init__(company,model)
    def num_wheel(self):
        return 2

    def engine_type(self):
        return "honda 70cc"

c=Car("Toyota",2012)
print(c.detail())
print(c.engine_type())
