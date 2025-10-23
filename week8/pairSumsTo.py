import time

def pairSumsToUgly(L, n):
    for x in L:
        for y in L:
            if x + y == n:
                return True
    return False

def pairSumsToBad(L, n):
    for x in L:
        if n - x in L:
            return True
    return False
    
def pairSumsToGood(L, n):
    S = set(L)
    for x in L:
        if n - x in S:
            return True
    return False


f = open("1M_primes.txt")
numList=[]
for s in f.read().split():
    numList.append(int(s))

numList = numList[:10000] # try 10k numbers, 1M is too much for ugly and bad


#n = 94956 # it's not worst case
n = 94957

print(f"Testing one case with len(L) = {len(numList)} and  n = {n}")
print("-"*40)
start = time.time()
result = pairSumsToUgly(numList,n )  
timeElapsed = time.time() - start

print(f'"Ugly" version returned "{result}" in {timeElapsed:0.4f} seconds')


start = time.time()
result = pairSumsToBad(numList, n)  
timeElapsed = time.time() - start

print(f'"Bad" version returned "{result}" in {timeElapsed:0.4f} seconds')


start = time.time()
result = pairSumsToGood(numList, n)  
timeElapsed = time.time() - start

print(f'"Good" version returned "{result}" in {timeElapsed:0.4f} seconds')



