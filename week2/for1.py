# break: stop before reaching the end of the range
def playWithRange(n):
    for i in range(n, 0, -1): # backwards
        print("Hi #", i)
        if i % 5 == 0:  # stop as soon as you find a multiple of 5
            break
    print("Done")
    
playWithRange(42)