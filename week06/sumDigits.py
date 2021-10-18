""" write the recursive function sumDigits(n) that returns the sum of the digits in n """
def sumDigit(n):
    if n < 10:
        return n
    lastDigit = n % 10
    result = lastDigit + sumDigit( n//10)
    return result
    
print(sumDigit(15112))
    
    
    
"""
    sumDigit(15112)
                2 + sumDigit(1511)
                          1       + sumDigit(151)
                                       1         + sumDigit(15)
                                                      5          + sumDigit(1)
                                                                        1      
                                                                             
"""
                                                                      
        
    
  