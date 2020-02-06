def bookExample(filename):
    f = open(filename, "r")
    bookText = f.read()
    print(bookText)
    f.close()
    
def bookExampleAgain(filename):
    with open(filename, "r") as f:
        bookText = f.read()
        print(bookText)
    # after the with, f.close() is called automatically
    
def bookThief(filename):
    with open(filename, "r") as f:
        bookText = f.read()
        
        bookText = bookText.replace("Alice", "Hermione")
        bookText = bookText.replace("ALICE", "HERMIONE")
        bookText = bookText.replace("White Rabbit", "House Elf")
        bookText = bookText.replace("Rabbit", "Elf")
        bookText = bookText.replace("Lewis Carroll", "Ryan Riley")
        
        with open("newBook.txt", "w") as outFile:
            outFile.write(bookText)
          
#bookThief("alice.txt")
            
def groupParsing(theFile):
    retList = []
    with open(theFile, "r") as f:
        for line in f:
            line = line.rstrip()
            colonSplit = line.split(":")
            #print(colonSplit)
            lineSplit = colonSplit[1].split(",")
            
            for i in range(len(lineSplit)):
                lineSplit[i] = lineSplit[i].strip()
            
            retList.append(lineSplit)

    return retList
            
            
theList = groupParsing("groups.txt")
print(theList)
        