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
    
    
class Poodle(Dog):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def dance(self):
        print(f"{self.name} dances!")
        
    def bark(self):
        print(f"Poodle Dog says Woof!")
    
d = Dog("Elf", 4)
print(d)

p = Poodle("Poodle", 5, "brown")
print(p.name)
print(p)#__repr__
print(p.bark())
p.dance()

#d.dance() #crashes

########## Type AND IsInstance ###########
print("Type")
#Type() - checks class type of object 
print(type(d) == Dog)  # T
print(type(p) == Poodle)  # T
print(type(p) == Dog) # F
print(type(d) == Poodle) # F

print("isinsatnce")
#isinstance() - checks inheritence
print(isinstance(d, Dog))  # T
print(isinstance(p, Poodle))  # T
print(isinstance(p, Dog)) # T
print(isinstance(d, Poodle)) # F





