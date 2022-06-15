def printL(L,indexsofar=0):
    if L==[]:
        return
    print(f"index: {indexsofar} {L[0]}")
 
    return printL(L[1:], indexsofar+1)

printL([7,3,5,1,4,2])