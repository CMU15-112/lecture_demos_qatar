class Book():
    def __init__(self, title, author, year, copies):
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies
    def __eq__(self, other):
        return self.title.lower() == other.title.lower() and \
               self.author == other.author and \
               self.year == other.year
    def __hash__(self):
        return hash( (self.title.lower(), self.author, self.year) )
        


book1 = Book("Hello 112", "Eduardo Feo", 2022, 7)
book2 = Book("hello 112", "Eduardo Feo", 2022, 7)
book3 = Book("hello 112", "Eduardo Feo", 2022, 4)

print("Check equality:", book1 == book2, book1 == book3)


bookset = set()
bookset.add(book1)

print("Book2 in bookset", book2 in bookset)

