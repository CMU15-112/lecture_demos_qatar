# continue: ignore the rest of the loop body and move to the next in the range
def playWithRange(n):
    for i in range(n, 0, -1): # backwards
        if i % 5 == 0:  # go back to the top
            continue
        print("Hi #", i)
    print("Done")
    
playWithRange(42)