########################## (==) VS (is)
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b) # True: == checks values (content)
print(a is b) # False is checks aliases

################# __eq__ 
class Dog(object):
    
    def __init__(self, dName, dAge):
        self.name = dName
        self.age = dAge
        self.woofCount = 0

    def __eq__(self, other):
        return type(self) == type(other) and self.name == other.name and self.age == other.age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def __repr__(self):
        return f"{self.name} is {self.age} years old"

d1 = Dog("Elf", 4)
d2 = Dog("Elf", 4)

# Gives False if __eq__ is not defined in the class
    # Python doesn't know how to compare objects of my class by default
print(d1 == d2) #calls __eq__ 
print(d1 is d2)

print(d1 == 4) #crashes if type is not checked in __eq__ method


################# __str__ or __repr__
print(d1) #__str__

d3 = Dog("Dot", 7)
l = [d1, d2, d3]
print(l) #__repr__
