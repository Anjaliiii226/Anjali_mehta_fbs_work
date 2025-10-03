class Product:
    discount = 10 
    def __init__(self, pid=None, pname=None, price=0.0, quantity=0):
        self.pid = pid
        self.pname = pname
        self.price = price
        self.quantity = quantity
        print(f"Product object created with ID: {self.pid}")
    def __del__(self):
        print(f"Product object with ID {self.pid} is deleted.")

    def ShowProduct(self):
        print("Product Details:")
        print(f"ID       : {self.pid}")
        print(f"Name     : {self.pname}")
        print(f"Price    : {self.price}")
        print(f"Quantity : {self.quantity}")
        print("-" * 30)

    def apply_discount(self):
        discount_amount = (Product.discount / 100) * self.price
        self.price = self.price - discount_amount
        print(f"Discount of {Product.discount}% applied. New price: {self.price}")

p1 = Product(201, "Laptop", 50000, 2)
p1.ShowProduct()
p1.apply_discount()
p1.ShowProduct()

p2 = Product()
p2.ShowProduct()

Product.discount = 20
p3 = Product(202, "Smartphone", 30000, 5)
p3.apply_discount()
p3.ShowProduct()
