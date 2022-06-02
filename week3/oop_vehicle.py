class Vehicle(object):
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.counter = 0  # initialize counter here!!
        
        # 10 other lines
        
    def addPassenger(self, passenger):
        if self.counter < self.capacity:
            self.counter += 1
            return True
        return False
      
    def removePassenger(self):
        if self.counter > 0:
            self.counter -= 1
            return True
        return False
    
    def __repr__(self):
        return f"{self.name} contains {self.counter}"    
    
class Harley(Vehicle):
    def __init__(self):
        super().__init__("Harley Davidson", 2)
    def __repr__(self):
        return f"{self.name} is great and contains {self.counter}"    
        
    
# You can create a vehicle with a name and capacity
v = Vehicle("Row Boat", 2)
assert(str(v) == "Row Boat contains 0")
# You can add passengers up to the capacity. The following two lines each
# add a passenger.
assert(v.addPassenger("Ken") == True)
assert(v.addPassenger("Barbie") == True)
assert(str(v) == "Row Boat contains 2")
# Once the vehicle is full, you can't add any more passengers.
assert(v.addPassenger("Ted") == False)
assert(str(v) == "Row Boat contains 2")
# Remove the most recently added passenger.
assert(v.removePassenger() == True)
assert(str(v) == "Row Boat contains 1")
# If a passenger is removed, then space is freed up to add another one.
assert(v.addPassenger("Ted") == True)
assert(str(v) == "Row Boat contains 2")
# You can't remove a passenger from an empty vehicle
assert(v.removePassenger() == True)
assert(v.removePassenger() == True)
assert(v.removePassenger() == False)
assert(str(v) == "Row Boat contains 0")
print("Passed! for Vehicle")

# A Harley is a vehicle with name "Harley Davidson" and capacity 2
m = Harley()
assert(str(m) == "Harley Davidson is great and contains 0")
assert(m.addPassenger("Noor")==True)
assert(m.addPassenger("Ali")==True)
assert(m.addPassenger("Ahmed")==False)
assert(str(m) == "Harley Davidson is great and contains 2")
assert(isinstance(m, Harley))
assert(isinstance(m, Vehicle))
print("Passed! for Harley")
        