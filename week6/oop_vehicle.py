######## Complete the class definition below ########
class Vehicle(object):
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.passengers = []
    def addPassenger(self, passenger):
        if len(self.passengers) < self.capacity:
            self.passengers.append(passenger)
            return True
        else:
            return False
    def removePassenger(self):
        # Complete below
        pass
    def __repr__(self):
        return f"{self.name} contains {len(self.passengers)}"

# Define class Harley

# You can create a vehicle with a name and capacity
v = Vehicle("Row Boat", 2)
print(v)
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

# A Harley is a vehicle with name "Harley Davidson" and capacity 2
m = Harley()
assert(str(m) == "Harley Davidson contains 0")
assert(m.addPassenger("Noor")==True)
assert(m.addPassenger("Ali")==True)
assert(m.addPassenger("Ahmed")==False)
assert(str(m) == "Harley Davidson contains 2")
assert(isinstance(m, Harley))
assert(isinstance(m, Vehicle))
