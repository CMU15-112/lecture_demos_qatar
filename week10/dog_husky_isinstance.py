class Dog(object):
    def __init__(self, name):
        self.name = name


class Husky(Dog):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
d = Dog('Fred')
h = Husky('Max', 5)

print(type(d)) # <class '__main__.Dog'>
print(type(h)) # <class '__main__.Husky'>
print(isinstance(h, type(d))) # True
print(isinstance(h, type(d))) # True

