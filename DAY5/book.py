class book:
    def __init__(self, title, author):
        self.name = title
        self.author = author
    def display(self):
        print("Book Name:", self.name)
        print("Author Name:", self.author)
b1=book(input("Enter Book Name: "), input("Enter Author Name: "))
b1.display()