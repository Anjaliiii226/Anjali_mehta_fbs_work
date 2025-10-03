class Shirt:

    size_price_factor = {
        "small": 1.0,     
        "medium": 1.1,   
        "large": 1.2,    
        "xlarge": 1.3    
    }
    def __init__(self, sid=None, sname=None, stype=None, price=0.0, size="small"):
        self.sid = sid
        self.sname = sname
        self.stype = stype
        self.price = price
        self.size = size.lower() if size else "small"

        self.apply_size_pricing()
        print(f"Shirt object created with ID: {self.sid}")

    def __del__(self):
        print(f"Shirt object with ID {self.sid} is deleted.")
    def ShowShirt(self):
        print("Shirt Details:")
        print(f"ID     : {self.sid}")
        print(f"Name   : {self.sname}")
        print(f"Type   : {self.stype}")
        print(f"Size   : {self.size}")
        print(f"Price  : {self.price}")
        print("-" * 30)

    def apply_size_pricing(self):
        if self.size in Shirt.size_price_factor:
            self.price = self.price * Shirt.size_price_factor[self.size]
        else:
            print("Invalid size! Defaulting to small.")
            self.size = "small"
