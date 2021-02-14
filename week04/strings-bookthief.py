def bookThief(filename):
    
    #f = open(filename, "r")
    with open(filename, "r") as f:
        bookText = f.read()
        
    bookText = bookText.replace("Alice", "Hermione")
    bookText = bookText.replace("White Rabbit", "Black Cat")
    bookText = bookText.replace("Rabbit", "Cat")
    bookText = bookText.replace("rabbit", "cat")
    bookText = bookText.replace("Lewis Carroll", "Ryan Riley")
           
    with open("newBook.txt","w") as outFile:
        outFile.write(bookText)
    
    #f.close()
        
        
bookThief("alice.txt")
        