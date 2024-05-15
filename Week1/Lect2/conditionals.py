def condFunc(n):
    if n > 0:
        print("n is +")
    else:
        print("n is -")
        
condFunc(3)
condFunc(-3)

def nestedCond(n1, n2):    
    if n1 > 0:       
        if n2 > 0:
            print("Both are +")
        else: # n2 <0
            print("n1 is + and n2 is -")
    else: #n1 <0
        if n2 > 0:
            print("n1 is - and n2 is +")
        else: # n2 <0
            print("Both are -")
            
nestedCond(3, 3)
nestedCond(-3, -3)
nestedCond(3, -3)
nestedCond(-3, 3)

def betterFunc(n1, n2):
    
    if n1 > 0 and n2 > 0:
            print("Both are +")
    elif n1 > 0 and n2 < 0:
            print("n1 is + and n2 is -")
    elif n1 < 0 and n2 > 0:
            print("n1 is - and n2 is +")
    else:
            print("Both are -")






        
            