def printMysteryStarShape(n):
    for i in range(n):
        print(i,end="")
        for j in range(i):
            if i%2 ==0:
                print(' *', end="")
            else:
                print(' -', end="")
        # I'm done printing stars for line i
        print()
        
        
        
printMysteryStarShape(5)