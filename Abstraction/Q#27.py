from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, emp_id, emp_name):
        self.emp_id = emp_id
        self.emp_name = emp_name
    def employee(self):
         print(f"""
         Employee ID    : {self.emp_id}
         Employee  Name : {self.emp_name}
         
         """)

    @abstractmethod
    def calculate_salary(self):
        pass


class FullTimeEmployee(Employee):
    def __init__(self, emp_id, emp_name, salary):
        super().__init__(emp_id, emp_name)
        self.salary = salary

    def calculate_salary(self):
        print("Full time employee salary : ",self.salary)


class PartTimeEmployee(Employee):
    def __init__(self, emp_id, emp_name, hours_worked, hourly_rate):
        super().__init__(emp_id, emp_name)
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_salary(self):
        print("Part time employee salary : ", self.hours_worked * self.hourly_rate)


ft_employee = FullTimeEmployee("FT001", "Ali Khan", 50000)
pt_employee = PartTimeEmployee("PT001", "Hassan ali", 20, 15)
ft_employee.calculate_salary()
pt_employee.calculate_salary()

