class Library:
    def __init__(self, book, author, price):
        self.book = book
        self.author = author
        self.price = price

    def add_book(self):
        print("\nBook added to the library")

    def show_book(self):
        print("\nBook Name:", self.book)
        print("Author:", self.author)
        print("Price:", self.price)

    def update_price(self, new_price):
        self.price = new_price
        print("\nPrice Updated")

    def delete_book(self):
        self.book = "No book found"
        self.author = "No author found"
        self.price = "No price found"
        print("\nBook Deleted")


book = input("Enter Book Name: ")
author = input("Enter Author Name: ")
price = int(input("Enter Price: "))

l = Library(book, author, price)
l.add_book()
l.show_book()
new_price = int(input("\nEnter New Price: "))
l.update_price(new_price)
l.show_book()
l.delete_book()
l.show_book()