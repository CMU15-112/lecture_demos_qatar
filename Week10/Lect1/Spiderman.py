class SpiderMan(object):
    
    def __init__(self, name):
        self.name = name
        self.hp = 100
        
    def shootWeb(self):
        return f"{self.name} shoots a web"
    
    def takeDamage(self, d):
        self.hp -= d
        return f"{self.name} gets hit for {d} hp"
    
    def __repr__(self):
        return f"SpiderMan({self.name}) with {self.hp} hp"
    
    def __eq__(self, other):
        return type(self) == type(other) and self.name == other.name
    
s = SpiderMan("Peter")
assert(str(s) == "SpiderMan(Peter) with 100 hp")
assert(s == SpiderMan("Peter"))
assert(s != SpiderMan("Bob"))
assert(s != 42)
assert(s != "SpiderMan(Peter) with 100 hp")
assert(s.shootWeb() == "Peter shoots a web")
assert(s.takeDamage(25) == "Peter gets hit for 25 hp")
assert(str(s) == "SpiderMan(Peter) with 75 hp")
assert(s == SpiderMan("Peter"))