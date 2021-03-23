class Pet(object):
    def __init__(self, name):
        self.name = name
        
    def makeSound(self):
        pass
    
class Dog(Pet):
    def makeSound(self):
        print(f"{self.name}: Woof!")
        
class Cat(Pet):
    def makeSound(self):
        print(f"{self.name}: Meow!")

class Poodle(Dog):
    def makeSound(self):
        print(f"Poodle {self.name}: Woof!")    

c = Cat("Fluffy")
d = Dog("Fido")
c.makeSound()
d.makeSound()

print(type(c))
print(type(d))

# Polymorphism: c is actually BOTH a Pet and a Cat
print(isinstance(c,Cat))
print(isinstance(c,Dog))
print(isinstance(c,Pet))
print("---")
print(type(c) == Cat)
print(type(c) == Pet)
print("---")
p = Poodle("Francis")
print(isinstance(p,Pet))
print(isinstance(p,Dog))
print(isinstance(p,Poodle))
print(isinstance(p,Cat))
print(type(p))

L = [c, 56, "Joe", d, False, p]

# Count the number of pets in the list (wrong)
cnt = 0
for item in L:
    if type(item) == Pet:
        cnt += 1
print(f"There are {cnt} pets in the list")

# Count the number of pets in the list (right)
cnt = 0
for item in L:
    if isinstance(item, Pet):
        cnt += 1
print(f"There are {cnt} pets in the list")