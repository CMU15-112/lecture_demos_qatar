class SpiderMan(object):
    
    def __init__(self, name):
        
        self.name= name
        self.hp=100
        
        
    def shootWeb(self):
        return f"{self.name} shoots a web"
    
    def takeDamage(self, damage):
        self.hp-=damage
        return f"{self.name} gets hit for {damage} hp"
        
    def __eq__(self, other):
        return (type(other)==type(self)) and (self.name == other.name)
    
    def __repr__(self):
        return f"SpiderMan({self.name}) with {self.hp} hp"
        

s = SpiderMan("Peter")
assert(str(s) == "SpiderMan(Peter) with 100 hp")
# SpiderMen can be equal to each other. This considers the name, but not the hp
assert(s == SpiderMan("Peter"))
assert(s != SpiderMan("Bob"))
assert(s != 42)
assert(s != "SpiderMan(Peter) with 100 hp")
# SpiderMan can shoot a web
assert(s.shootWeb() == "Peter shoots a web")
# SpiderMan can get hurt
assert(s.takeDamage(25) == "Peter gets hit for 25 hp")
assert(str(s) == "SpiderMan(Peter) with 75 hp")
# Current hp doesn't impact equivalence
assert(s == SpiderMan("Peter"))

