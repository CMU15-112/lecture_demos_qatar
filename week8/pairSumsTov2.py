import time

# Find two elements of the list that sum to n
# If no pair exists, return None
def pairSumsToNv2(L, n):
    for n1 in L: # loop N times
        if n - n1 in L:
            return (n1, n - n1)
    return None



f = open("100Knumbers.txt")
numList=[]
for s in f.read().split():
    numList.append(int(s))

print(f"Loaded {len(numList)} numbers")

start = time.time()
print(f'Pair that sums to 94956 {pairSumsToNv2(numList, 94956)}')
print(f'Pair that sums to 94957 {pairSumsToNv2(numList, 94957)}')

end = time.time()
elapsed1 = end - start
print("List-based v1\nFinished in {:0.4f} seconds".format(elapsed1))
