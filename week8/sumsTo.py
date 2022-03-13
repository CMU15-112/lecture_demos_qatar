import time


# Find two elements of the list that sum to n
# If no pair exists, return None
def pairSumsToNv0(L, n):
    for n1 in L:
        for n2 in L:
            if n1 + n2 == n:
                return (n1, n2)
    return None

def pairSumsToNv1(L, n):
    for n1 in L:
        if n-n1 in L:
            return (n1, n-n1)
    return None
    
def pairSumsToNv2(L, n):
    mySet = set(L)
    for n1 in L:
        if n-n1 in mySet:
            return (n1, n-n1)
    return None

f = open("1M_primes.txt")
numList=[]
for s in f.read().split():
    numList.append(int(s))
    
print(f"Loaded {len(numList)} numbers")
    
#start = time.time()
#print(pairSumsToNv0(numList, 94956))
#print(pairSumsToNv0(numList, 94957))
#end = time.time()
#elapsed1 = end - start
#print("List-based v0\nFinished in {:0.4f} seconds".format(elapsed1))

#start = time.time()
#print(pairSumsToNv1(numList, 94956))
#print(pairSumsToNv1(numList, 94957))
#end = time.time()
#elapsed1 = end - start
#print("List-based v1\nFinished in {:0.4f} seconds".format(elapsed1))

start = time.time()
print(pairSumsToNv2(numList, 94956))
print(pairSumsToNv2(numList, 94957))
end = time.time()
elapsed1 = end - start
print("Set-based v1\nFinished in {:0.4f} seconds".format(elapsed1))