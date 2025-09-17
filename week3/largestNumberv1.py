def largestNumberv1(s):
    maxnum=None
    currentNumStr = ""
    for c in s:
        if c.isdigit():
            currentNumStr = currentNumStr + c
        else:
            if currentNumStr != "":
                number = int(currentNumStr)
                if maxnum==None:
                    maxnum=number
                maxnum=max(maxnum, number)                
                currentNumStr = ""
    if currentNumStr != "":
        number = int(currentNumStr)
        if maxnum==None:
            maxnum=number
            maxnum=max(maxnum, number)  
    return maxnum
    
def testLargestNumber():
    print("Testing largestNumber...",end="")
    assert(largestNumberv1("I saw 3 dogs, 17 cats, and 14 cows!")==17)
    assert(largestNumberv1("I saw four dogs")==None)
    assert(largestNumberv1("This is difficult15112case")==15112)
    assert(largestNumberv1("This is difficult15112")==15112)
    print("passed")
    
testLargestNumber()