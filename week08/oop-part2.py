class Hexagon(object):
    def __init__(self, s):
        self.s = s
        
    def __repr__(self):
        return f"Hexagon(s={self.s})"
    
    def __eq__(self, other):
        return isinstance(other, Hexagon) and self.s == other.s
    
    def __hash__(self):
        return hash(self.s)
    
    def getArea(self):
        return self.s ** 2 * (3 * (3 ** 0.5)) / 2
    
h = Hexagon(5)
print(h.getArea())
print(h)

print(h == Hexagon(6))
print(h == Hexagon(5))
print(h == "Monkey")

mySet = set()
mySet.add(h)
mySet.add(Hexagon(6))
mySet.add(Hexagon(10))
print(mySet)
print(Hexagon(7) in mySet)
print(Hexagon(10) in mySet)