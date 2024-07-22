class Car:
    def __init__(self, model, year, price):
        self.model = model
        self.year = year
        self.price = price

    def display_details(self):
        print(f"Car Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Price: ${self.price}")

    def calculate_depreciation(self, owned_years):
        if owned_years <= 0:
            depreciation = 0
        else:
            depreciation_rate_per_year = 0.15
            depreciation = self.price * depreciation_rate_per_year *owned_years

        depreciated_value = self.price - depreciation
        return depreciated_value

car1 = Car("Toyota Camry", 2020, 30000)
car1.display_details()

years_owned = 3
depreciated_value = car1.calculate_depreciation(years_owned)
print(f"After {years_owned} years, the depreciated value of the car is ${depreciated_value}")
