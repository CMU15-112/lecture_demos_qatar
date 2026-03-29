class Dog(object):

    nextID = 1 # class-level attribute
    
    def __init__(self, dName, dAge):
        self.name = dName
        self.age = dAge
        self.woofCount = 0
        self.id = Dog.nextID
        Dog.nextID += 1

d1 = Dog("Elf", 4)
#nextID = 2
print(f"d1 ID: {d1.id}")

d2 = Dog("Brownie", 5)
#nextID = 3
print(f"d2 ID: {d2.id}")

d3 = Dog("Dot", 3)
#nextID = 4
print(f"d3 ID: {d3.id}")

print(d1.nextID) #4
print(d2.nextID) #4
print(d3.nextID) #4
print(Dog.nextID) #4
#nextID is one copy that belongs to the class and
    #can be accessed through any instance

