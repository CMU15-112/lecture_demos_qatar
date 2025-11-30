import random
import math

class Clock:
    # this is a class variable (it's shared across all instances)
    randomColors = ['blue', 'yellow', 'red', 'green', 'pink']
    def __init__(self, clockId, radius=50, canvasSize=600):
        dirs = [-1, 1]
        self.id = clockId
        self.speed = 10  # fixed for now
        self.canvasSize = canvasSize
        self.cx = random.randint(radius, self.canvasSize -  radius)
        self.cy = random.randint(radius, self.canvasSize -  radius)
        self.dx = dirs[random.randint(0,1)]
        self.dy = dirs[random.randint(0,1)]
        self.radius = radius
        self.color = Clock.randomColor()

        
    # this is a class method (note it doesn't get self)
    # it's normally used for functions that do not depend on
    # one particular instance
    def randomColor():
        return Clock.randomColors[random.randint(0,len(Clock.randomColors)-1)]
    
    def randomizeColor(self):
        self.color = Clock.randomColor()
    # updates the clock position according to the current speed
    # retrieves the canvas dimensions and speed from the model
    def step(self):
        self.cx += self.speed * self.dx
        if self.cx + self.radius > self.canvasSize:
            self.cx = self.canvasSize - self.radius
            self.dx  *= -1
        elif self.cx <= self.radius:
            self.cx = self.radius
            self.dx  *= -1

        # vertical movement
        self.cy  += self.speed * self.dy
        if self.cy >= (self.canvasSize - self.radius):
             self.cy = self.canvasSize - self.radius
             self.dy *= -1
        elif self.cy <= self.radius:
             self.cy = self.radius
             self.dy *= -1
             
    def pointInsideClock(self, x, y):
        return ((self.cx - x)**2 + (self.cy - y)**2) <= self.radius**2
    def asDict(self):
        return {'id': self.id, 'cx': self.cx, 'cy': self.cy, 'color': self.color} 
  
