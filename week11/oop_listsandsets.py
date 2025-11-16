"""
From F21, exam 2
"""

class Book(object):
    def __init__(self, title, author, year, copies):
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies
        self.avail = copies
    def __eq__(self, other):
        return self.title.lower() == other.title.lower() and self.author == other.author \
               and self.year == other.year
    def __hash__(self):
        return hash((self.title.lower(),self.author,self.year))
    def __str__(self):
        return f'{self.author}, "{self.title}", {self.year}, {self.avail}/{self.copies}'


# A book has a title, authors, and publication year
# It also has a number of copies in the library,
# and the number of copies currently available
b1 = Book("The Art of Computer Programming",
              "Donald Knuth", 1968, 5)
assert(str(b1) == """Donald Knuth, "The Art of Computer Programming", 1968, 5/5""")
# When determining equality, book titles are not case sensitive, but author
# is. Also, the number of copies doesn't matter.
b2 = Book("The C Programming Language",  "Kernighan and Ritchie", 1978, 10)
b3 = Book("the c programming language",  "Kernighan and Ritchie", 1978, 8)
b4 = Book("THE C PROGRAMMING LANGUAGE",  "Kernighan and Ritchie", 1978, 10)
b5 = Book("THE C PROGRAMMING LANGUAGE",  "kernighan and Ritchie", 1978, 10)
b6 = Book("The C Programming Language",  "Kernighan and Ritchie", 1988, 10)
assert(b2 == b3)
assert(b2 == b4)
assert(b4 != b5)
assert(b2 != b6)
# You should be able to hash books. The rules follow those for equality.
collection = set()
collection.add(b1)
collection.add(b2)
assert(b1 in collection)
assert(b2 in collection)
assert(b3 in collection)
assert(b4 in collection)
assert(b5 not in collection)
assert(b6 not in collection)


