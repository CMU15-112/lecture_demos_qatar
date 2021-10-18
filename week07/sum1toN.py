#  n >= 1
def sum1ToN(n):
    if n==1:
        return 1
    cumulativeSum = n + sum1ToN(n-1)
    return cumulativeSum
    
    
print(sum1ToN(5))
    
    
""" sum1toN(n) = n + sum1ToN(n-1)
                 n-1 + sum1ToN(n-2)
                       n-2 + sum1ToN(n-3)
                       
   for example:
    sum1ToN(3)  = 3 + sum1ToN(2) [3]
                        2        + sum1ToN(1) [1]
                                      1       + sum1ToN(0) [0]
                                      
"""