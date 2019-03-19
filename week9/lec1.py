# Sum all the integers in L
def sumList(L):
    # Base case
    if len(L) == 1:
        return L[0]
    # Recursive case
    else:
        return L[0] + sumList(L[1:])
        
#print(sumList([1,2,3]))

def sumDigits(n):
    # Base case
    if n//10 == 0:
        return n
    # Recursive case
    else:
        return (n%10) + sumDigits(n//10)
        
#print(sumDigits(356))

def bob(n):
    print(n)
    m = bob(n-1)
    return m
    
#print(bob(10))

# Sums all the numbers in range [a,b]
def rangeSum(a, b):
    if a > b:
        return rangeSum(b,a)
    elif a == b:
        return a
    else:
        return a + rangeSum(a+1, b)
        
def fib(n, depth=0):
    print("  "*depth + "fib("+str(n)+")")
    if n == 0:
        print("  "*depth + "ret: "+str(0))
        return 0
    elif n == 1:
        print("  "*depth + "ret: "+str(1))
        return 1
    else:
        ret = fib(n-1, depth+1)+fib(n-2, depth+1)
        print("  "*depth + "ret: "+str(ret))
        return ret

class Cat(object):
    def __init__(self, name, breed, trained):
        self.name = name
        self.breed = breed
        self.trained = trained

class Dog(object):
    def __init__(self, dogsName, dogsBreed, isTrained):
        self.name = dogsName
        self.breed = dogsBreed
        self.trained = isTrained
        
    def __eq__(self, otherDog):
        return  isinstance(otherDog, Dog) and \
                self.name == otherDog.name and \
                self.breed == otherDog.breed and \
                self.trained == otherDog.trained

    def bark(self):
        print(self.name + ": bark!")
    
    def fetch(self):
        if self.trained == True:
            print(self.name + " fetched something")
        else:
            print(self.name + " sat there doing nothing")
            
    def sniff(self, otherDog):
        print(self.name + " sniffed " + otherDog.name)
        
myDog = Dog("Fido", "Terrier", False)
myOtherDog = Dog("Bruno", "Bull Dog", True)
myThirdDog = Dog("Fido", "Terrier", False)
myFourthDog = myDog

print(myDog.name, myDog.breed, myDog.trained)
print(myOtherDog.name, myOtherDog.breed, myOtherDog.trained)

print(myDog == myOtherDog)
print(myDog == myThirdDog)
print(myDog == myFourthDog)

myDog.bark()
myDog.fetch()
myOtherDog.bark()
myOtherDog.fetch()

myDog.sniff(myOtherDog)

myCat = Cat("fluffy", "prettycat", True)
myOtherCat = Cat("Fido", "Terrier", False)

print(myDog == myOtherCat)