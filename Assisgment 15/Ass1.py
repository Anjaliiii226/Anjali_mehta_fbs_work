class Book():
    def __init__(self,id=100,name="two state",price=300,author="Chetan bhagat"):
        print("Constructor calling")
        self.bid = id
        self.bname = name
        self.price = price
        self.author = author
    def showBook(self):
        print("Book id:",self.bid)
        print("Book name:",self.bname)
        print("Book price:",self.price)
        print("Book of author:",self.author)

    def __del__(self):
        print("destructor call")

obj1 = Book(101,"C in depth",450,"deepali srivastava")
obj1.showBook()
print("#####################")
obj2 = Book()
obj2.showBook()
