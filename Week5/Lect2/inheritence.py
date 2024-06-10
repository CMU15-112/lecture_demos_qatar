class Dog(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says Woof!")

    def fetch(self):
        print(f"{self.name} is fetching the ball.")
        
    def __repr__(self):
        return f"Dog {self.name} is {self.age} years old!"
    
    
class Poodle(Dog): #subclass
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color
        
    def dance(self):
        return f"Poodle Dances"
    
    def bark(self):
        print(f"Poodle says Woof!")
 


d = Dog("Elf", 4)
print(d)

p = Poodle("Poodle", 5, "brown")
print(p)
print(p.color)
p.bark()
print(p.dance())
#print(d.dance()) # CRASHES

#Type() - returns the class of the object without considering inheritance
print(type(d) == Dog)  # T
print(type(p) == Dog) # F
print(type(p) == Poodle) # T
print(type(d) == Poodle) # F

#isinstance() - checks for inheritance
print(isinstance(d, Dog))  # T
print(isinstance(p, Dog)) # T **
print(isinstance(p, Poodle)) # T
print(isinstance(d, Poodle)) # F





