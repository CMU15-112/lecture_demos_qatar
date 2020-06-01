# some primes
primelist = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229]

print(len(primelist))

# check if element is in the list
print("2 in primelist?", 2 in primelist)
print("\"2\" in primelist?", "2" in primelist)

print("4 in primelist?", 4 in primelist)

# count occurrences
print("Occurrences of number 13?", primelist.count(13))
print("Occurrences of number 14?", primelist.count(14))

print("what's the position of number 13?=", primelist.index(13))  #
# don't ask the position of an element if you are not sure it is there
#print("what's the position of number 14?=", primelist.index(14))
#print("what's the position of number mytext?=", primelist.index("my text"))

# index (only if element is there)
l=[1,2,3,3,4,2]
l.index(2)

# 0-based, even if you start don't start looking from 0
l.index(2,2)

#this is different as we are creating a new list with l[2:]
print(l[2:].index(2))

#print("Index of 13, starting from 10=", primelist.index(13,10))
