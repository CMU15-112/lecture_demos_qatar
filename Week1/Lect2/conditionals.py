def conditionalFunction(x):
    if x>=0:
        print("x is positive")
    else:
        print("x s negative")
        
    print("Thanks for asking")
    
    
conditionalFunction(2)
print("------------")
conditionalFunction(-1)
print("------------")


##  nested conditionals
def nestedConditional(x, y):
    if x >= 0:
        if y >= 0:
            print("both are positive")
        else:
            print("x is positive, y is negative")
    else: #x is negaitve
        if y >= 0:
            print("x is negative, y is positive")
        else:
            print("both negative")
    print("Done with code")
          
print("First Case:")
nestedConditional(1,2)
print("Second Case:")
nestedConditional(1,-2)
print("Third Case:")
nestedConditional(-1,2)
print("Fourth Case:")
nestedConditional(-1,-2)
            
    
        
print("-----------")
def betterFunction(x,y):
    if x>=0 and y>=0:
        print("both are positive")
    elif x>=0 and y<0:
        print("x is positive, y is negative")
    elif x<0 and y>=0:
        print("x is negative, y is positive")
    else:
        print("both negative")
    print("Done")

print("First Case:")
betterFunction(1,2)
print("Second Case:")
betterFunction(1,-2)
print("Third Case:")
betterFunction(-1,2)
print("Fourth Case:")
betterFunction(-1,-2)
            

        