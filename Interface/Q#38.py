from abc import ABC,abstractmethod
class Payable(ABC):
    @abstractmethod
    def pay(self):
        pass
class Invoice(Payable):
    def __init__(self,invoice_no):
        self.invoice_no=invoice_no
    def pay(self):
        print(f"Invoice number is : {self.invoice_no}")
class Salary(Payable):
    def __init__(self,name,salary):
        self.name = name
        self.salary=salary
    def pay(self):
        print(f"Name is {self.name}\nSalary is {self.salary}")
class Subscription(Payable):
    def __init__(self,name,subscription):
        self.name = name
        self.subscription = subscription
    def pay(self):
        print(f"Name is {self.name}\n Subscription is {self.subscription}")

iv = Invoice("1e231")
iv.pay()
s =Salary("ali",3000)
s.pay()
sub = Subscription("abbas","manager")
sub.pay()
