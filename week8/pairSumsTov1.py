import time

# Find two elements of the list that sum to n
# If no pair exists, return None
def pairSumsToNv1(L, n):
    for n1 in L: # loop N times
        for n2 in L:  # loop N times (nested)
            if n1 + n2 == n:
                return (n1, n2)
    return None



f = open("100Knumbers.txt")
numList=[]
for s in f.read().split():
    numList.append(int(s))

print(f"Loaded {len(numList)} numbers")

start = time.time()
print(f'Pair that sums to 94956 {pairSumsToNv1(numList, 94956)}')
print(f'Pair that sums to 94957 {pairSumsToNv1(numList, 94957)}')

end = time.time()
elapsed1 = end - start
print("Set-based v1\nFinished in {:0.4f} seconds".format(elapsed1))
