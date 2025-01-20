def is7ish(n):
   n =abs(n)
   sum =0
   while n!=0:
       sum += n%10
       n = n //10
   return sum%7==0

def nth7ish(n):
    needToFind = n+1
    foundSoFar = 0
    guess = -1
    
    while foundSoFar < needToFind:
        guess += 1  # make a guess
        if is7ish(guess):  # check
            foundSoFar += 1
            print(guess, "is 7ish, found so far:", foundSoFar)
            last7ishFound = guess
        else:
            print(guess, "is NOT 7ish")
    return last7ishFound
    
nth7ish(6) 
    
#assert(nth7ish(0) == 0)
#assert(nth7ish(1) == 7)
#assert(nth7ish(6) == 52)