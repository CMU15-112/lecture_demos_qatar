# 22220022211, d=2 -> find 222 

def longestDigitRun(n, d):  # partial, find length of the first run
    #print ("longest ", n)
    counter = 0
    maxcounter = 0
    if n ==0 and d==0:
        return 1
    while n > 0:
        currentDigit = n%10
        if currentDigit == d:
            counter += 1
        else:
            if counter > 0:
                #print("we found a run")
                maxcounter = max(counter, maxcounter)
                counter = 0 # we are resetting run
                
                #return counter
        n = n // 10
    
    return max(counter, maxcounter)
            


print(longestDigitRun(2220022211,2)==3) # 3
print(longestDigitRun(2,2)==1) # 1
print(longestDigitRun(1122,2)==2) # 2
print(longestDigitRun(345,2)==0) # 0
print(longestDigitRun(345,0)==0) # 0
print(longestDigitRun(0,0)==1) # 0




    