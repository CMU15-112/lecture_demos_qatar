class vehicle():
    def __init__(self,mk="",md=1970,sp=0,cl="White"):
        self.make = mk
        self.model = 0
        self.setModel(md)
        self.speed = sp
        self.started = False
        self.color = cl
    def __str__(self):
        result = "Make:" + self.make +"\n"
        result += "Model:" + str(self.model) +"\n"
        result += "Color:" + self.color +"\n"
        result += "Current Speed:" + str(self.speed) +"\n"
        return result
    def __repr__(self):
        result = "Make:" + self.make +"\t"
        result += "Model:" + str(self.model) +"\t"
        result += "Color:" + self.color +"\t"
        result += "Current Speed:" + str(self.speed)
        return result
    def setModel(self,newmodel):
        if newmodel > 1920:
            self.model = newmodel
    def startVehicle(self):
        if not self.started:
            self.started = True
            self.speed = 0
    def turnOffVehicle(self):
        self.started = False
        self.speed = 0
    def changeSpeed(self,delta):
        if self.started and (self.speed + delta >= 0):
            self.speed += delta
            
car1 = vehicle("Toyota",2020,0,"Black")
car2 = vehicle("Lexus", 2012,40,"Pink")
car3 = vehicle()
car3.setModel(1900)
print (car1)
car1.changeSpeed(40)
print (car1)
car1.startVehicle()
car1.changeSpeed(50)
print (car1)






