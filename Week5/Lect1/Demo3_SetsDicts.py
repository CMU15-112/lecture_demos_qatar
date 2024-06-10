class Dog(object):
    
    def __init__(self, dName, dAge):
        self.name = dName
        self.age = dAge
        self.woofCount = 0
        
    def __hash__(self):
        return hash((self.name, self.age)) # 1 immutable argument
    
    def __eq__(self, other):
        return (type(other) == type(self)) and (self.name == other.name) and (self.age == other.age)
 
        
s = set()
s.add(Dog("Elf", 4))
print(Dog("Elf", 4) in s)

d1 = Dog("Elf", 4)
print(hash(d1))
print(hash(Dog("Elf", 4)))

