class Product:
    def __init__(self,name,price,stock_quantity):
        self.__name = name
        self.__price = price
        self.__stock_quantity = stock_quantity

    def get_name(self):
        print(f" Product Name : {self.__name}")
    def set_name(self,new_name):
        self.__name=new_name
        print(f"Product new name is: ",self.__name)

    def get_price(self):
        print(f" {self.__name} price is : {self.__price} each")

    def set_price(self, new_price):
        self.__price = new_price
        print(f"{self.__name} new price is: ", self.__price," each")

    def get_stock(self):
        if self.__stock_quantity>0:
         print(f" Stock quantity of {self.__name} in store is [ {self.__stock_quantity} ]")
        else:
            print(f"Stock quantity of {self.__name} in store is [ {self.__stock_quantity} ]")

    def set_stock(self, new_stock):
        self.__stock_quantity=new_stock
        if self.__stock_quantity>0:
         print(f" Stock quantity of {self.__name} in store is [ {self.__stock_quantity} ]")
        else:
            print(f"Stock quantity of {self.__name} in store is [ {self.__stock_quantity} ]")



p = Product(["apple","mango","watermellon"],120,4)
p.get_name()
p.get_price()
p.set_name(["apple","banana","Grapes"])
p.set_price(300)