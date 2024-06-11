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
    
    def __hash__(self):
        return hash((self.name))
    
    def __eq__(self, other):
        return (type(self) == type(other)) and (self.name == other.name)
    
class TobeySpiderMan(SpiderMan):
    
    def __init__(self):
        super().__init__("Tobey")
        self.hasVenomSuit = False
        
    def venomAttach(self):
        self.hasVenomSuit = True
        
    def venomDetach(self): 
        if self.hasVenomSuit:
            self.hasVenomSuit = False
            return True
        
        return False
    
    def takeDamage(self, d):
        if self.hasVenomSuit:
            return super().takeDamage(d//2)
        else:
            return super().takeDamage(d)
        
class AndrewSpiderMan(SpiderMan):
    
    def __init__(self, fluid=2):
        super().__init__("Andrew")
        self.webFluid = fluid
        
    def shootWeb(self):
        if self.webFluid > 0:
            self.webFluid -= 1
            return super().shootWeb()
        else:
            return f"{self.name} is out of web fluid!"

    def refillWebFluid(self, n):
        self.webFluid += n
        
        
############### TEST CASES #################################
s = SpiderMan("Peter")
print(str(s))
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

# TobeySpiderMan is a SpiderMan
t = TobeySpiderMan()
assert(isinstance(t, SpiderMan))
assert(str(t) == "SpiderMan(Tobey) with 100 hp")
# TobeySpiderMan has some special properties when taking damage
# Normally, he takes damage just like any other SpiderMan
assert(t.takeDamage(10) == "Tobey gets hit for 10 hp")
assert(str(t) == "SpiderMan(Tobey) with 90 hp")
# But, if he is wearing a Venom suit, then he only takes half damage
t.venomAttach()
assert(t.takeDamage(10) == "Tobey gets hit for 5 hp")
assert(str(t) == "SpiderMan(Tobey) with 85 hp")
# He can take off the Venom suit
assert(t.venomDetach() == True)
print(t.hasVenomSuit)
assert(t.takeDamage(10) == "Tobey gets hit for 10 hp")
assert(str(t) == "SpiderMan(Tobey) with 75 hp")
# But if he isn't wearing the Venom suit, then he can't take it off
assert(t.venomDetach() == False)
# Equivalence between TobeySpiderMen only considers the name, not the hp
assert(t == TobeySpiderMan())
assert(t != 42)
assert(t != "SpiderMan(Tobey) with 75 hp")
# But a TobeySpiderMan is never equal to a SpiderMan, even if the names are the same
assert(t != SpiderMan("Tobey"))
assert(SpiderMan("Tobey") != t)
# Other than this, he is a normal SpiderMan
assert(t.shootWeb() == "Tobey shoots a web")

# AndrewSpiderMan is a SpiderMan, but TobeySpiderMan and AndrewSpider are not
# instances of each other
a = AndrewSpiderMan()
assert(isinstance(a, SpiderMan))
assert(not isinstance(a, TobeySpiderMan))
assert(not isinstance(t, AndrewSpiderMan))
assert(str(a) == "SpiderMan(Andrew) with 100 hp")

# AndrewSpiderMan has a special property when shooting webs: He has a limited
# supply of web fluid.  By default he can only shoot webs twice before needing
# to refill.
assert(a.shootWeb() == "Andrew shoots a web")
assert(a.shootWeb() == "Andrew shoots a web")
assert(a.shootWeb() == "Andrew is out of web fluid!")
a.refillWebFluid(3)
for i in range(3):
    assert(a.shootWeb() == "Andrew shoots a web")
assert(a.shootWeb() == "Andrew is out of web fluid!")

# When creating an AndrewSpiderMan, you can specify his initial web fluid capacity
a2 = AndrewSpiderMan(10)
for i in range(10):
    assert(a2.shootWeb() == "Andrew shoots a web")
assert(a2.shootWeb() == "Andrew is out of web fluid!")    
# Equivalence between AndrewSpiderMen only considers the name, not the hp or webfluid
assert(a == AndrewSpiderMan())
assert(a2 == AndrewSpiderMan())
assert(a == a2)
assert(a != 42)
assert(a != "SpiderMan(Andrew) with 100 hp")
# But an AndrewSpiderMan is never equal to a SpiderMan, even if the names are the same
assert(a != SpiderMan("Andrew"))
assert(SpiderMan("Andrew") != a)
# Other than this, he is a normal SpiderMan
assert(a.takeDamage(25) == "Andrew gets hit for 25 hp")
assert(str(a) == "SpiderMan(Andrew) with 75 hp")

# SpiderMen of all kinds can be put into a Set and retrieved later.
spiderSet = set()
spiderSet.add(s)
spiderSet.add(t)
spiderSet.add(a)
assert(SpiderMan("Peter") in spiderSet)
assert(TobeySpiderMan() in spiderSet)
assert(AndrewSpiderMan() in spiderSet)
print("PASSED !!")
