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
    
    def __hash__(self):
        return hash(self.name)


class TobeySpiderMan(SpiderMan):
    
    def __init__(self):
        #self.name = "Tobey"
        #self.hp = 100
        super().__init__("Tobey")
        self.venomSuit = False
        
    def venomAttach(self):
        self.venomSuit = True
        
    def takeDamage(self, dmg):
        if self.venomSuit:
            return super().takeDamage(dmg//2)
        else:
            return super().takeDamage(dmg)

    def venomDetach(self):
        if self.venomSuit:
            self.venomSuit = False
            return True
        
        return False
   

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
        
        
def testSpiderManClasses():
    print('Testing SpiderMan classes...', end='')

    # Basic SpiderMan
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

    # TobeySpiderMan is a SpiderMan
    t = TobeySpiderMan()
    assert(isinstance(t, SpiderMan))
    assert(str(t) == "SpiderMan(Tobey) with 100 hp")
    # Normally takes damage like any other SpiderMan
    assert(t.takeDamage(10) == "Tobey gets hit for 10 hp")
    assert(str(t) == "SpiderMan(Tobey) with 90 hp")
    # With Venom suit, takes half damage
    t.venomAttach() #changes attribute
    assert(t.takeDamage(10) == "Tobey gets hit for 5 hp") #override
    assert(str(t) == "SpiderMan(Tobey) with 85 hp")
    # Can take off the Venom suit
    assert(t.venomDetach() == True)  # T/F?, changes attribute
    assert(t.takeDamage(10) == "Tobey gets hit for 10 hp")
    assert(str(t) == "SpiderMan(Tobey) with 75 hp")
    # Can't detach if not wearing it
    assert(t.venomDetach() == False)
    # Equivalence only considers name
    assert(t == TobeySpiderMan())
    assert(t != 42)
    assert(t != "SpiderMan(Tobey) with 75 hp")
    # TobeySpiderMan is never equal to a SpiderMan
    assert(t != SpiderMan("Tobey"))
    assert(SpiderMan("Tobey") != t)
    # Otherwise a normal SpiderMan
    assert(t.shootWeb() == "Tobey shoots a web")

#     # AndrewSpiderMan is a SpiderMan, but not a TobeySpiderMan
#     a = AndrewSpiderMan()
#     assert(isinstance(a, SpiderMan))
#     assert(not isinstance(a, TobeySpiderMan))
#     assert(not isinstance(t, AndrewSpiderMan))
#     assert(str(a) == "SpiderMan(Andrew) with 100 hp")
#     # Limited web fluid, default 2 shots
#     assert(a.shootWeb() == "Andrew shoots a web")
#     assert(a.shootWeb() == "Andrew shoots a web")
#     assert(a.shootWeb() == "Andrew is out of web fluid!")
#     a.refillWebFluid(3)
#     for i in range(3):
#         assert(a.shootWeb() == "Andrew shoots a web")
#     assert(a.shootWeb() == "Andrew is out of web fluid!")
#     # Can specify initial web fluid capacity
#     a2 = AndrewSpiderMan(10)
#     for i in range(10):
#         assert(a2.shootWeb() == "Andrew shoots a web")
#     assert(a2.shootWeb() == "Andrew is out of web fluid!")
#     # Equivalence only considers name
#     assert(a == AndrewSpiderMan())
#     assert(a2 == AndrewSpiderMan())
#     assert(a == a2)
#     assert(a != 42)
#     assert(a != "SpiderMan(Andrew) with 100 hp")
#     # AndrewSpiderMan is never equal to a SpiderMan
#     assert(a != SpiderMan("Andrew"))
#     assert(SpiderMan("Andrew") != a)
#     # Otherwise a normal SpiderMan
#     assert(a.takeDamage(25) == "Andrew gets hit for 25 hp")
#     assert(str(a) == "SpiderMan(Andrew) with 75 hp")
# 
#     # All kinds can be added to a set
#     spiderSet = set()
#     spiderSet.add(s)
#     spiderSet.add(t)
#     spiderSet.add(a)
#     assert(SpiderMan("Peter") in spiderSet)
#     assert(TobeySpiderMan() in spiderSet)
#     assert(AndrewSpiderMan() in spiderSet)

    print('Passed.')

if __name__ == '__main__':
    testSpiderManClasses()