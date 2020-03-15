class Pet(object):
    def __init__(self, name):
        self.name = name
        
    def makeSound(self):
        pass
    
class Dog(Pet):
        
    def makeSound(self):
        print(f"{self.name}: Woof")
        
class Poodle(Dog):
    
    def makeSound(self):
        print(f"{self.name}: <annoying> woof!")
        
class Cat(Pet):
    
    def makeSound(self):
        print(f"{self.name}: meow")
        
class Calico(Cat):
    
    def makeSound(self):
        print(f"{self.name}: <slightly orange> meow")
        

petList = []

samplePet = Pet("Bob")
petList.append(samplePet)

d = Dog("Rover")
petList.append(d)

p = Poodle("Fido")
petList.append(p)

myCat = Cat("Fluffy")
petList.append(myCat)

myCal = Calico("Thundercat")
petList.append(myCal)

# Polymorphism
dogCount = 0
for pet in petList:
    if isinstance(pet, Dog):
        dogCount += 1
    pet.makeSound()
print(f"I found {dogCount} dogs!")
    
print(type(samplePet))
print(type(samplePet) == Pet)

print(type(p))
print(type(p) == Pet)
print(isinstance(p, Poodle))
print(isinstance(p, Dog))
print(isinstance(p, Pet))
print(isinstance(p, Cat))