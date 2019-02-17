def bookThief():
    with open("alice.txt", "r") as f:
        bookText = f.read()
        
        bookText = bookText.replace("Lewis Carroll", "Ryan Riley")
        bookText = bookText.replace("Alice", "Hermione")
        bookText = bookText.replace("ALICE", "HERMIONE")
        bookText = bookText.replace("White Rabbit", "House Elf")
        bookText = bookText.replace("Rabbit", "Elf")
        
        with open("newBook.txt", "w") as outFile:
            outFile.write(bookText)
        
bookThief()