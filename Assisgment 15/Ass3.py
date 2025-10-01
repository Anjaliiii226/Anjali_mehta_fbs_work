class Shirt():
    def __init__(self,id=100,name="max",type="casual",price=1000,size="small"):
        print("Constructor calling")
        self.sid = id
        self.sname = name
        self.type = type
        self.price = price
        self.size = size

    def showShirt(self):
        print("Shirt id :",self.sid)  
        print("Shirt name :",self.sname)
        print("Shirt type :",self.type)
        print("Shirt price :",self.price)
        print("Shirt size :",self.size)

    def __del__(self):
        print("Destructor calling")

obj1 = Shirt(101,"raymond","Formal",1500,"Medium")
obj1.showShirt()
print("####################")
obj2 = Shirt()
obj2.showShirt()