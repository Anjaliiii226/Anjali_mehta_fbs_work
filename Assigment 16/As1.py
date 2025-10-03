class Book:
   
    count = 0

   
    def __init__(self, eid=None, ename=None, price=None, author=None):
        self.eid = eid
        self.ename = ename
        self.price = price
        self.author = author
        
        Book.count += 1
        print(f"Book object created. Current count: {Book.count}")

    def __del__(self):
        print(f"Book object with ID {self.eid} is deleted.")

    def ShowBook(self):
        print("Book Details:")
        print(f"ID     : {self.eid}")
        print(f"Name   : {self.ename}")
        print(f"Price  : {self.price}")
        print(f"Author : {self.author}")
        print("-" * 30)

b1 = Book(101, "Python Programming", 450, "Guido")
b1.ShowBook()

b2 = Book()
b2.ShowBook()

b3 = Book(102, "Data Science", 650, "Wes McKinney")
b3.ShowBook()

print("Total books created:", Book.count)
del b2
