import time

# Find two elements of the list that sum to n
# If no pair exists, return None
def pairSumsToNv3(L, n):
    mySet = set(L)
    for n1 in L: # loop N times
        if n - n1 in mySet:
            return (n1, n - n1)
    return None



f = open("1Mnumbers.txt")
numList=[]
for s in f.read().split():
    numList.append(int(s))

print(f"Loaded {len(numList)} numbers")

start = time.time()
print(f'Pair that sums to 94956 {pairSumsToNv3(numList, 94956)}')
print(f'Pair that sums to 94957 {pairSumsToNv3(numList, 94957)}')

end = time.time()
elapsed1 = end - start
print("Set-based v1\nFinished in {:0.4f} seconds".format(elapsed1))
