class Product():
    def __init__(self,id=100,name="laptop",price=50000,quantity=2):
        print("Constructor calling")
        self.pid=id
        self.pname=name
        self.price=price
        self.quantity=quantity

    def showProduct(self):
        print("Product id",self.pid)
        print("Product name",self.pname)
        print("Product price",self.price)
        print("Product quantity",self.quantity)

    def __del__(self):
        print("Destructor calling")
       
obj1=Product(101,"Mobile",250000,5)
obj1.showProduct()
print("###################")
obj2=Product()
obj2.showProduct()