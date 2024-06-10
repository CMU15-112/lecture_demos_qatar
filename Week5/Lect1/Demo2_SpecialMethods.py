class Dog(object):
    
    def __init__(self, dName, dAge):
        self.name = dName
        self.age = dAge
        self.woofCount = 0
        
    def __eq__(self, other):
        return (type(other) == type(self)) and (self.name == other.name) and (self.age == other.age)
    
    #def __str__(self):  # doesn't work for lists
        #return f"{self.name} is {self.age} years old"
    
    def __repr__(self): 
        return f"{self.name} is {self.age} years old"
    
d1 = Dog("Elf", 4)
d2 = Dog("Elf", 4)

print(d1==d2)

d3 = d1
print(d1 == d3)

print(d1 == 4)

print(d1)
print(str(d1))

d3= Dog("Dot", 7)
l = [d1, d3]
print(l)