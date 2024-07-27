class Product:
    def __init__(self, name, price, stock_quantity):
        self.name = name
        self.price = price
        self.stock_quantity = stock_quantity


class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.shopping_cart = []
class Order:
    def __init__(self, order_id, customer, products):
        self.order_id = order_id
        self.customer = customer
        self.products = products


class EcommercePlatform:
    def __init__(self):
        self.products = []
        self.customers = []
        self.orders = []

    def add_product(self, name, price, stock_quantity):
        product = Product(name, price, stock_quantity)
        self.products.append(product)
        print(f"  Name : {name} Price ; Rs.{price}/- Stock Quantity : {stock_quantity}")

    def register_customer(self, name, email):
        customer = Customer(name, email)
        self.customers.append(customer)
        print(f" Name : {name} Email : {email}")

    def place_order(self, customer, products):
        order_id = len(self.orders) + 1
        order = Order(order_id, customer, products)
        self.orders.append(order)
        print(f"Order {order_id} placed successfully!")

    def check_product_availability(self, product_name):
        for product in self.products:
            flag = False
            if product.name == product_name:
                flag = True
                if product.stock_quantity > 0:
                    print(f"Product {product_name} is available in stock")
                    break
                else:
                     print(f"Product {product_name} is out of stock")
        if (flag == True):
            print(f"Product {product_name} is available")
        else:
            print(f"Product {product_name} is not exist")


e = EcommercePlatform()

product1 = Product("Apple", 12, 6)
product2 = Product("Orange", 20, 6)

customer1 = Customer("Ali", "ali2gmail.com")
customer2 = Customer("Araiz Israr", " araiz12@gmail.com")

order1 = Order("IE-2", "Araiz", "Orange")
e.add_product(product1.name, product1.price, product1.stock_quantity)
e.add_product(product2.name, product2.price, product2.stock_quantity)
e.register_customer(customer1.name, customer1.email)
e.register_customer(customer2.name, customer2.email)
e.place_order(customer1, order1)


