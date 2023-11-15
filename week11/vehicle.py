class Vehicle:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.passengers = []

    def __repr__(self):
        ret = f"{self.name} contains {len(self.passengers)}:"
        for p in self.passengers:
            ret += f" {p}"
        return ret

    def addPassenger(self, name):
        if len(self.passengers) >= self.capacity:
            return False
        self.passengers.append(name)
        return True

    def removePassenger(self):
        if len(self.passengers) > 0:
            self.passengers.pop()
            return True
        else:
            return False

class Motorcycle(Vehicle):

    def __init__(self):
        super().__init__("Motorcycle", 1)
        self.up = False

    def popWheelie(self):
        self.up = True

    def stopWheelie(self):
        self.up = False

    def removePassenger(self):
        if self.up == True:
            return False
        return super().removePassenger()
