
class Dog(object): 

    nextID=0 #class attribute


    def __init__(self, name, age): 
        self.name = name 
        self.age = age
        self.woofCount=0

        Dog.nextID+=1
        self.ID= Dog.nextID

    def sayHi(self): 
        print(f"Hi, my name is {self.name} and I am {self.age} years old!")

    # This method takes a second parameter -- times 
    def bark(self, times): 
        print(f'{self.name} says: {"woof!" * times}') 
        self.woofCount += times # Then we can set and get the property in this method
        
        
    def __eq__(self, other):
        return type(other)==type(self) and self.name==other.name and self.age==other.age

    def __repr__(self):
        return f"Dog {self.name} is {self.age} years old"

    def gethashables(self):
        return (self.name, self.age)

    def __hash__(self):
        return hash(self.gethashables())
    
class Poodle(Dog):
    
    def __init__(self, name, age, furColor):
        super().__init__(name, age)
        self.furColor= furColor
        
    def dance(self):
        print(f"POODLE {self.name} DANCE !!")
    
    def bark(self, times):
        print(f" POODLE {self.name} WOOF {times} times ")

d= Dog("Elf", 4)
p= Poodle("Brownie", 6, "White")

print(d)
print(p)

d.bark(3)
p.bark(5)
p.dance()

#d.dance()


print("TYPE()")
print(type(d)== Dog)
print(type(p)== Dog)
print(type(d)== Poodle)
print(type(p)== Poodle)


print("isinstance()")
print(isinstance(d, Dog))
print(isinstance(p, Dog))
print(isinstance(d, Poodle))
print(isinstance(p, Poodle))