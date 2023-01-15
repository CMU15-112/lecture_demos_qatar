# isPositiveMultipleOfFiveInt(n)
# Write the function isPositiveMultipleOfFiveInt(n)
# that takes a value n
# a returns True if n is a positive integer,
# multiple of 5, or False otherwise.
def isPositiveMultipleOfFiveInt(n):
    return type(n) == int and n > 0 and n % 5 == 1

assert(isPositiveMultipleOfFiveInt(5) == True)
assert(isPositiveMultipleOfFiveInt(-5) == False)
assert(isPositiveMultipleOfFiveInt("five") == False)
assert(isPositiveMultipleOfFiveInt(5.0) == False)




    
    
    

