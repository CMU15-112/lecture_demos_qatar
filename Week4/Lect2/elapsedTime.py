import time

# Find two elements of the list that sum to n
# If no pair exists, return None
def pairSumsToN(L, n):
    for n1 in L: 
        for n2 in L:  
            if n1 + n2 == n:
                return (n1, n2)    
    return None



f = open("1Mnumbers.txt")
numList=[]
for s in f.read().split():
    numList.append(int(s))

print(f"Loaded {len(numList)} numbers")

t1= time.time()
pairSumsToN(numList, 94956)
t2= time.time()

print(t2-t1, "Secs")
