# Incomplete
# Try to complete it by yourself~

class Vehicle:
    def __init__(self, name, cap):
        self.name = name
        self.cap = cap
        self.pas = []
    def __repr__(self):
        return f"Row Boat contains {len(self.pas)}:"
    
    def addPassenger(self,pName):
        if len(self.pas) == self.cap:
            return False
        self.pas.append(pName)
        return True
        
    
    
    
class Motorcycle(Vehicle):
    pass
    
# You can create a vehicle with a name and capacity
v = Vehicle("Row Boat", 2)
assert(str(v) == "Row Boat contains 0:")

# You can add passengers up to the capacity. The following two lines each
# add a passenger.
assert(v.addPassenger("Ken") == True)
assert(v.addPassenger("Barbie") == True)
                     
assert(str(v) == "Row Boat contains 2: Ken Barbie")

# Once the vehicle is full, you can't add any more passengers.
assert(v.addPassenger("Ted") == False)
assert(str(v) == "Row Boat contains 2: Ken Barbie")

# Remove the most recently added passenger.
assert(v.removePassenger() == True)
assert(str(v) == "Row Boat contains 1: Ken")

# If a passenger is removed, then space is freed up to add another one.
assert(v.addPassenger("Ted") == True)
assert(str(v) == "Row Boat contains 2: Ken Ted")

# You can't remove a passenger from an empty vehicle
assert(v.removePassenger() == True)
assert(v.removePassenger() == True)
assert(v.removePassenger() == False)
assert(str(v) == "Row Boat contains 0:")

# A Motorcycle is a vehicle with an assumed name of Motorcycle and
# a capacity of 1
m = Motorcycle()
assert(str(m) == "Motorcycle contains 0:")
assert(m.addPassenger("Ken") == True)
assert(m.addPassenger("Ted") == False)
assert(str(m) == "Motorcycle contains 1: Ken")

# A motorcycle is both a Motorcycle and a Vehicle
assert(isinstance(m, Motorcycle) == True)
assert(isinstance(m, Vehicle) == True)

# While a motorcycle is doing a wheelie, you can't remove a passenger
m.popWheelie()
assert(m.removePassenger() == False)
assert(str(m) == "Motorcycle contains 1: Ken")

# Once the wheelie stops, you can remove as usual
m.stopWheelie()
assert(m.removePassenger() == True)
assert(str(m) == "Motorcycle contains 0:")