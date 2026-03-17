########## empty class
# class Dog(object):
#     pass
# 
# 
# d1 = Dog()
# d2 = Dog()
# 
# print(type(d1))
# print(isinstance(d2, Dog))
#         
# ##### Set and get properties
#             #(aka 'fields' or 'attributes') of these instances: 
#       
# d1.name = "Simba"
# d1.age = 5
# print(f"D1 {d1.name} and {d1.age}")
# 
# d2.name = "Brownie"
# d2.age = 4
# print(f"D2 {d2.name} and {d2.age}")

##### PRELOADING INSTANCES WIHT ATTRIBUTES

class Dog(object):
    
#     def constructor(dog, name, age):
#         dog.name = name
#         dog.age = age
        
    def __init__(self, name, age):
        self.name = name
        self.age = age     
        self.woofCount = 0

    def sayHi(self):
        print(f" Hi, My Name is {self.name}")

    def bark(self, times):
        print(f"{self.name} says {'Woof!'*times}")
        self.woofCount += times


d1 = Dog("Simba", 5) #calls __init__
print(f"D1 {d1.name} and {d1.age}")


d2 = Dog("Brownie", 4)
print(f"D2 {d2.name} and {d2.age}")


######## Methods

## function syntax - doesn't work
# def sayHi(dog):
#     print(f" Hi, My Name is {dog.name}")
# 
# sayHi(d1)

d1.sayHi()
d2.sayHi()

print(f"D2 {d2.name} woofed {d2.woofCount} times" )
d2.bark(3)
print(f"D2 {d2.name} woofed {d2.woofCount} times" )




