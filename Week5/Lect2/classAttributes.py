class Dog(object):
    
    nextID = 0

    def __init__(self, dName, dAge):
        self.name = dName
        self.age = dAge
        self.woofCount = 0
        self.id = Dog.nextID
        Dog.nextID += 1
        
    def __hash__(self):
        return hash((self.name, self.age)) # 1 immutable argument
    
    def __eq__(self, other):
        return (type(other) == type(self)) and (self.name == other.name) and (self.age == other.age)

d1 = Dog("Elf", 4)
print(f"d1 ID: {d1.id}")
d2 = Dog("Brownie", 5)
print(f"d2 ID: {d2.id}")
d3 = Dog("Dot", 3)
print(f"d3 ID: {d3.id}")

