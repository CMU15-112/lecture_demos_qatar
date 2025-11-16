class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"Hi, my name is {self.name} \
         and I am {self.age} years old."

    def __str__(self):
        return self.name
    
    def __repr__(self):
        return str(self)
    

p1 = Person("Hassan", 10)
p2 = Person("Sara", 12)

print(p1)
print(p2)
L = [p1, p2]
print(L)




