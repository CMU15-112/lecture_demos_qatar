import copy

class Dog(object):
    
    def __init__(self, dName, dAge):
        self.name = dName
        self.age = dAge
        self.woofCount = 0

    def __hash__(self):
        return hash( (self.name, self.age) ) #immutable data type (str, tuples, primitive)
        
    def __eq__(self, other):
        return type(self) == type(other) and self.name == other.name and self.age == other.age

 
   
s = set()
s.add(Dog("Elf", 4))
print(Dog("Elf", 4) in s)

d1 = Dog("Elf", 4)
print(hash(d1)) #__hash__
print(hash(Dog("Elf", 4)))

### Aliasing and copies
d2 = d1
print(d2 is d1)

d3 = copy.copy(d1)
print(d3 is d1)