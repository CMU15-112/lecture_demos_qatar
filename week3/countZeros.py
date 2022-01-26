# define countZeros(n) gets a integer number n and returns the number of zero digits in n
def countZeros(n):
    count = 0
    n = abs(n)
    if n == 0:
        return 1
    # n is strictly positive
    while n != 0:
        lastDigit = n%10
        # check if it is zero
        if lastDigit == 0:
            count += 1
        n = n//10
    return count
        
    

def testCountZeros():
    print("Testing countZeros...")
    # Define some test cases here
    assert(countZeros(1020) == 2)
    assert(countZeros(1) == 0)
    assert(countZeros(-1020) == 2)
    assert(countZeros(-1) == 0)
    assert(countZeros(0) == 1)
    assert(countZeros(111111111111111111111) == 0)
    print("passed")
testCountZeros()

