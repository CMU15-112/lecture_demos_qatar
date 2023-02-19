class Vehicle:
    fleetSize = 0
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.numPassengers = 0
        Vehicle.fleetSize += 1

    def __repr__(self):
        return f"{self.name} contains {self.numPassengers}"
    def addPassenger(self, passengerName):  # myVehicle.addPassenger("Eduardo")
        if self.numPassengers == self.capacity:
            return False
        self.numPassengers += 1
        return True
    def getFleetSize():
        return Vehicle.fleetSize

class Harley(Vehicle):
    def __init__(self):
        super().__init__("Harley Davidson", 2)



# You can create a vehicle with a name and capacity
v = Vehicle("Row Boat", 2)
assert(str(v) == "Row Boat contains 0")

# You can add passengers up to the capacity. The following two lines each
# add a passenger.
assert(v.addPassenger("Ken") == True)
assert(v.addPassenger("Barbie") == True)
assert(str(v) == "Row Boat contains 2")
# # Once the vehicle is full, you can't add any more passengers.
assert(v.addPassenger("Ted") == False)
assert(str(v) == "Row Boat contains 2")


########## You need to expand the class to pass these test cases

# # Remove the most recently added passenger.
# assert(v.removePassenger() == True)
# assert(str(v) == "Row Boat contains 1")
# # If a passenger is removed, then space is freed up to add another one.
# assert(v.addPassenger("Ted") == True)
# assert(str(v) == "Row Boat contains 2")
# # You can't remove a passenger from an empty vehicle
# assert(v.removePassenger() == True)
# assert(v.removePassenger() == True)
# assert(v.removePassenger() == False)

assert(Vehicle.getFleetSize() == 1)  # counts how many vehicles I have in my garage
#assert(str(v) == "Row Boat contains 0")


# # A Harley is a vehicle with name "Harley Davidson" and capacity 2
m = Harley()
assert(str(m) == "Harley Davidson contains 0")
assert(Vehicle.getFleetSize() == 2)
assert(m.addPassenger("Noor")==True)
assert(m.addPassenger("Ali")==True)
assert(m.addPassenger("Ahmed")==False)
assert(str(m) == "Harley Davidson contains 2")
assert(isinstance(m, Harley))
assert(isinstance(m, Vehicle))
