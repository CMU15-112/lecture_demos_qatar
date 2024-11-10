class Toy:
    def __init__(self, owner):
        self.owners = [owner]
        
    def getOwners(self):
        return ",".join(self.owners)
    
    def addOwner(self, o):
        self.owners.append(o)
        self.owners.sort()
        
    def __repr__(self):
        return f"Toy (owner={self.getOwners()})"
    
    def __eq__(self, o):
        return type(self) == type(o) and self.owners == o.owners

class Stuffie(Toy):
    def __init__(self, owner, name):
        super().__init__(owner)
        self.name = name
    
    def __repr__(self):
        return f"Stuffie (name={self.name}, owner={self.getOwners()})"
    
    def __eq__(self, o):
        return type(self) == type(o) and self.name == o.name \
               and self.owners == o.owners

def testToyClass():
    # A basic toy has an owner
    t = Toy("Susy")
    assert(t.getOwners() == "Susy")
    assert(str(t) == "Toy (owner=Susy)")
    # Toys can also have more than one owner
    t.addOwner("Johnny")
    t.addOwner("Zed")
    t.addOwner("Albus")
    # The order the owners are listed matters...
    assert(t.getOwners() == "Albus,Johnny,Susy,Zed")
    assert(str(t) == "Toy (owner=Albus,Johnny,Susy,Zed)")
    # Toy properly handles equivalence checking
    n = Toy("Johnny")
    n.addOwner("Albus")
    n.addOwner("Susy")
    n.addOwner("Zed")
    assert(t == n)
    assert(t != Toy("Billy"))
    assert(t != "Johnny")    
    
    # A basic stuffie has an owner and a name
    s = Stuffie("Hamoodie", "MyBear")
    assert(str(s) == "Stuffie (name=MyBear, owner=Hamoodie)")
    # Stuffies, like Toys, can also have multiple owners
    s.addOwner("Fatima")
    # Just like Toys, order of owners listed matters...
    assert(s.getOwners() == "Fatima,Hamoodie")
    assert(str(s) == "Stuffie (name=MyBear, owner=Fatima,Hamoodie)")
    # Stuffie properly handles equivalence checking
    s = Stuffie("Hamoodie", "MyBear")
    assert(s == Stuffie("Hamoodie", "MyBear"))
    assert(s != Toy("Hamoodie"))
    assert(s != Stuffie("Billy", "MyBear"))
    assert(s != Stuffie("Hamoodie", "YourBear"))
    assert(s != 42)
    assert(Toy("Bob") != Stuffie("Bob", "MyBear"))

    # Verify some inheritance rules...
    assert(isinstance(t, Toy) == True)
    assert(isinstance(t, Stuffie) == False)
    assert(isinstance(s, Toy) == True)
    assert(isinstance(s, Stuffie) == True)
    
testToyClass()