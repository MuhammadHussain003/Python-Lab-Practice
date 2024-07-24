class Appilance:
    def __init__(self,company_name,no_of_power_use,no_of_hour_use):
        self.no_of_power_use = no_of_power_use
        self.no_of_hour_use = no_of_hour_use
        self.company_name = company_name

    def power_usage(self):
        pass
class WashingMachine(Appilance):
    def __init__(self,company_name,no_of_power_use,no_of_hour_use):
        super().__init__(company_name,no_of_power_use,no_of_hour_use)

    def power_usage(self):
        p_usage = self.no_of_power_use*self.no_of_hour_use
        print(f"Total Energy use in {self.no_of_hour_use} hour by {self.company_name} Washing Machine is {p_usage} watt ")


class Oven(Appilance):
    def __init__(self,company_name,no_of_power_use,no_of_hour_use):
        super().__init__(company_name,no_of_power_use,no_of_hour_use)
    def power_usage(self):
        p_usage = self.no_of_power_use * self.no_of_hour_use
        print(f"Total Energy use in {self.no_of_hour_use} hour by {self.company_name} Oven is {p_usage} watt ")


w = WashingMachine("Haier",6,4)
o = Oven("National",5,1)
w.power_usage()
o.power_usage()