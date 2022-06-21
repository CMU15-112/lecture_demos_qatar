import time

# Find any two elements of the list that sum to n
# If no pair exists, return None
# Example:
# pairSumsToN( [1,3,4,2,0], 2) == (2,0)
# pairSumsToN( [1,3,4,0,2], 10) == None
# pairSumsToN( [1,3,4,0,2], 6) == (4,2)

def pairSumsToNv0(L, n):
    for a in L:
        for b in L:
            if a == b:
                continue
            if a + b == n:
                return (a, b)
    return None

def pythonIn(L, x):
    return x in L

def myIn(L, x):
    for b in L:
        if b == x:
            return True
    return False

def pairSumsToNv1(L, n):
    for a in L:
        if myIn(L, n-a):  # for b in L: if b == n-a return True 
            return (a, n-a)
    return None

def pairSumsToNv2(L, n):
    mySet = set(L)
    for a in L:
        if n - a in mySet:
            return (a, n-a)
    return None

f = open("1M_primes.txt")
numList=[]
for s in f.read().split():
    numList.append(int(s))
    
start = time.time()
print(pairSumsToNv0(numList[:10000], 12))
#print(pairSumsToNv2(numList, 94957))
end = time.time()
elapsed1 = end - start
print("List v0\nFinished in {:0.4f} seconds".format(elapsed1))

start = time.time()
print(pairSumsToNv1(numList[:10000], 12))
#print(pairSumsToNv2(numList, 94957))
end = time.time()
elapsed1 = end - start
print("List v1\nFinished in {:0.4f} seconds".format(elapsed1))
    

start = time.time()
print(pairSumsToNv2(numList[:10000], 12))
#print(pairSumsToNv2(numList, 94957))
end = time.time()
elapsed1 = end - start
print("Set-based v2\nFinished in {:0.4f} seconds".format(elapsed1))
        
