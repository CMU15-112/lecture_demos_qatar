class Book(object):
    def __init__(self, title, author, year, copies):
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies
        self.avail = copies
    def __repr__(self):
        return '{}, "{}", {}, {}/{}'.format(self.author, self.title, self.year, self.avail, self.copies)
    def loan(self):
        if self.avail == 0:
            return False
        self.avail -= 1
        return True
    def getCopiesAvailable(self):
        return self.avail
    def returnCopy(self):
        if self.avail < self.copies:
            self.avail += 1
            
        
    def __eq__(self, other):
        return self.title.lower() == other.title.lower() and self.author == other.author and self.year == other.year
    def __hash__(self):
        return hash(self.title.lower()) + hash(self.author) + hash(self.year)

class Journal(Book):
    def __init__(self, title, year, copies):
        super().__init__(title, "Various Authors", year, copies)

# A book has a title, authors, and publication year
# It also has a number of copies in the library,
# and number of copies currently available
b1 = Book("The Art of Computer Programming",
              "Donald Knuth", 1968, 5)
assert(str(b1) == """Donald Knuth, "The Art of Computer Programming", 1968, 5/5""")
# You can loan a book, as long as there are copies available
assert(b1.loan() == True)
assert(b1.getCopiesAvailable() == 4)
assert(b1.loan() == True)
assert(b1.getCopiesAvailable() == 3)
for i in range(3):
    assert(b1.loan() == True)
assert(str(b1) == """Donald Knuth, "The Art of Computer Programming", 1968, 0/5""")
assert(b1.loan() == False) # no more copies available, return False
    

# You can return a library item
b1.returnCopy()
assert(b1.getCopiesAvailable() == 1)
b1.returnCopy()
assert(b1.getCopiesAvailable() == 2)
# if more copies than the initial number of copies are returned, they are discarded
for i in range(10):
    b1.returnCopy()
assert(b1.getCopiesAvailable() == 5)

# Book titles are not case sensitive
b2 = Book("The C Programming Language",  "Kernighan and Ritchie", 1978, 10)
b3 = Book("the c programming language",  "Kernighan and Ritchie", 1978, 10)
b4 = Book("THE C PROGRAMMING LANGUAGE",  "Kernighan and Ritchie", 1978, 10)
b5 = Book("The C Programming Language",  "Kernighan and Ritchie", 1988, 10)
assert(b2 == b3)
assert(b2 == b4)
assert(b2 != b5)

# A Journal is a book with various authors
j1 = Journal("Science Vol 374 Issue 6568", 2021, 8)
assert(str(j1) == """Various Authors, "Science Vol 374 Issue 6568", 2021, 8/8""")
assert(j1 != b1)
assert(isinstance(j1, Book))

# Finally, you should be able to hash books
collection = set()
collection.add(b1)
collection.add(b2)
assert(b3 in collection)
assert(b4 in collection)
assert(b5 not in collection)
collection.add(j1)
assert( len(collection) == 3)
print(":)")
