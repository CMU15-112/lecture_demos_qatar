# empty class
class Dog(object):
    
    def __init__(self, dName, dAge):
        self.name = dName
        self.age = dAge
        self.woofCount = 0
        
    def sayHi(self):
        print(f" Hi I am {self.name} and I am {self.age} years old")
        
    def bark(self, times):
        print(f"{self.name} says {'Woof!'*times}")
        self.woofCount += times



#d1 = Dog()
#d1.name = "Simba"
#d1.age = 5

d1 = Dog("Simba", 5) # preload instances with attribute values
print(type(d1))
print(isinstance(d1, Dog))
print(f"d1 name {d1.name} and age {d1.age}")
#sayHi(d1) # function call
d1.sayHi() # method call

#d2 = Dog()
#d2.name = "Brownie"
#d2.age = 4
d2 = Dog("Brownie", 4)
print(type(d2))
print(isinstance(d2, Dog))
print(f"d2 name {d2.name} and age {d2.age}")
#sayHi(d2)
d2.sayHi()

print(f"{d2.woofCount}")
d2.bark(3)
print(f"{d2.woofCount}")






