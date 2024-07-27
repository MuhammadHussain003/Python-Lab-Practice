class Product:
    def __init__(self,name , price , stock_quantity):
        self.name = name
        self.price = price
        self.stock_quantity = stock_quantity
class Supplier:
    def __init__(self,name , supplier_Id ):
        self.name = name
        self.supplier_Id = supplier_Id

class Inventory:
    products = []
    suppliers = []

    def add_products(self,product):
        self.products.append(product)
        print(f"""Name : {product.name} Price : ${product.price} Stock Quantity : {product.stock_quantity}""")
    def remove_products(self,product_name):
        for product in self.products:
            if product.name == product_name:
                self.products.remove(product)
                print(f"Product '{product_name}' removed successfully!")
                return
        print(f"Product '{product_name}' not found in the inventory.")

    def update_stock(self, product_name, new_quantity):
        for product in self.products:
            if product.name == product_name:
                product.stock_quantity = new_quantity
                print(product.stock_quantity)

    def add_supplier(self, supplier):
        self.suppliers.append(supplier)

    def generate_report(self):
        print("Inventory Report:")
        for product in self.products:
            print(f"Name: {product.name}, Price: ${product.price}, Stock Quantity: {product.stock_quantity}")
        print("Suppliers:")
        for supplier in self.suppliers:
            print(f"Name: {supplier.name}, Supplier ID: {supplier.supplier_Id}")

inventory = Inventory()

product1 = Product("apple",12,4)
product2 = Product("Orange",30,6)

supplier = Supplier("ali","e12")


inventory.add_products(product1)
inventory.add_products(product2)



inventory.update_stock("apple",12)

inventory.add_supplier(supplier)


inventory.generate_report()

