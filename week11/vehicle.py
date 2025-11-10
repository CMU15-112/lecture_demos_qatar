class Vehicle:
    def __init__(self, name):
        self.name = name
        self.moving = False
    def __repr__(self):
        res = f'{self.name}: '
        if not self.moving:
            return res + "stopped"
        else:
            return res +  "moving"
    def move(self):
        self.moving = True
    def brake(self):
        self.moving = False

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand + " " + model)
        self.towed = False
        self.towedVehicle = None
    def move(self):
        self.moving = True
        if self.towedVehicle != None:
            self.towedVehicle.move()
    def brake(self):
        if not self.towed:
            self.moving = False
            if self.towedVehicle != None:
                self.towedVehicle.moving = False
    def tow(self, other):
        if isinstance(other, Car):
            other.towed = True
            self.towedVehicle = other
            return True
        return False
    


# A Vehicle has a name
v1 = Vehicle("Millennium Falcon")
# A Vehicle is initially stopped
assert(str(v1) == "Millennium Falcon: stopped")
# A vehicle can move and brake
v1.move()
assert(str(v1) == "Millennium Falcon: moving")
v1.brake()
assert(str(v1) == "Millennium Falcon: stopped")
# A Car is a vehicle that has brand name and model
c1 = Car("Nissan", "Tiida")
assert(str(c1) == "Nissan Tiida: stopped")
c1.move()
assert(str(c1) == "Nissan Tiida: moving")
c1.brake()
assert(str(c1) == "Nissan Tiida: stopped")
c2 = Car("Toyota", "Land Cruiser")
assert(str(c2) == "Toyota Land Cruiser: stopped")
# A car can tow another car
assert(c2.tow(c1) == True)
assert(str(c1) == "Nissan Tiida: stopped")
assert(str(c2) == "Toyota Land Cruiser: stopped")
# when the towing car moves, the towed car also moves
c2.move()
assert(str(c1) == "Nissan Tiida: moving")
assert(str(c2) == "Toyota Land Cruiser: moving")
# the brakes don't work when the car is being towed
c1.brake()
assert(str(c1) == "Nissan Tiida: moving") # still moving
# when the towing car brakes, both cars stop
c2.brake()
assert(str(c1) == "Nissan Tiida: stopped")
assert(str(c2) == "Toyota Land Cruiser: stopped")
# Cars can only tow other cars
c3 = Car("Nissan", "Patrol")
assert(c3.tow(v1) == False) # we cannot tow the Millenium Falcon (it's not a car)
