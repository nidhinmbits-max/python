class Publisher:
    def __init__(self, publisher):
        self.publisher = publisher
class Book(Publisher):
    def __init__(self, publisher, title, author):
        super().__init__(publisher)
        self.title = title
        self.author = author
class Python(Book):
    def __init__(self, publisher, title, author, price, pages):
        super().__init__(publisher, title, author)
        self.price = price
        self.pages = pages
    def display(self):
        print("Book Details")
        print("Publisher:", self.publisher)
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)
        print("Number of Pages:", self.pages)
p = Python("DC books", "Rathri 12 manik shesham",
           "Akhil P Dharmjan", 450, 300)
p.display()

