def listFunc(L):
    L[0] = 5

def intFunc(n):
    n = 5
    
myList = [10]
myInt = 10

print(f"myList before: {myList}")
print(f"myInt before: {myInt}")

listFunc(myList)
intFunc(myInt)

print(f"myList after: {myList}")
print(f"myInt after: {myInt}")