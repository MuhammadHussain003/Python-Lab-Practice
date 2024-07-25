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
    order_id_counter = 0

    def __init__(self, customer, products):
        Order.order_id_counter += 1
        self.order_id = Order.order_id_counter
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
        print(f"Product '{name}' Price {price}  Stock Quantity {stock_quantity} ")

    def register_customer(self, name, email):
        customer = Customer(name, email)
        self.customers.append(customer)
        print(f"Customer '{name}' registered with email '{email}'.")

    def place_order(self, customer_name, product_names):
        products_to_order = []

        for c in self.customers:
            flag = False
            if c.name == customer_name:
                flag = True
                break
            else:
                flag = False

        if (flag == True):
            print(f"{customer_name} is already register so u can accept order..")
        else:
            print(f"{customer_name} is not found")
        for p in self.products:
            pak = False
            if p.name == product_names:
               pak = True
            for pr in self.products:
                   pr.stock_quantity>0


    #

    def check_product_availability(self, product_name):
        for prod in self.products:
            if prod.name == product_name:
                if prod.stock_quantity > 0:
                    print(f"Product '{product_name}' is available with {prod.stock_quantity} units in stock.")

                else:
                    print(f"Product '{product_name}' is out of stock.")

        print(f"Product '{product_name}' not found.")


e = EcommercePlatform()

p1 = Product("Grapes", 12, 4)
p2 = Product("apple", 18, 7)
c1 = Customer("Hussain", "hussain123@gmail.com")
c2 = Customer("Asif", "asif00@gmail.com")

print("\t\t\t\t\tProducts add \n")
e.add_product(p1.name, p1.price, p1.stock_quantity)
e.add_product(p2.name, p2.price, p2.stock_quantity)
print("\t\t\t\t\tRegister Customer \n")
e.register_customer(c1.name, c1.email)
e.register_customer(c2.name, c2.email)
e.place_order("Asif", "apple")
