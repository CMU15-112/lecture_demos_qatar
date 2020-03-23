from cmu_112_graphics import *
import random
class dot():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.color =  random.choice(["red","blue","green","pink","yellow","purple","orange","brown"])
        self.r = random.randint(5,10)
        self.dx = random.randint(-2,2)
        self.dy = random.randint(-2,2)
    def draw(self,canvas):
        canvas.create_oval(self.x-self.r,self.y-self.r,self.x+self.r,self.y+self.r,fill=self.color)
    def move(self,w,h):
        self.x += self.dx
        self.y += self.dy
        if self.x < 0 or self.x > w:
            self.dx = -self.dx
        if self.y < 0 or self.y > h:
            self.dy = -self.dy

def appStarted(app):
    app.counter = 0
    app.timerDelay = 100
    app.secondsDelay = 1000/app.timerDelay
    app.timerRunning = True
    app.allDots = []
    #pass


def timerFired(app): # The Controller
    #app.counter = app.counter + 1
    if app.timerRunning:
        updatedCounter(app)
    #if app.counter == 500:
    #    app.timerRunning = False
    if app.counter %5 == 0:
        d1 = dot(random.randint(1,app.width),random.randint(1,app.height))
        app.allDots.append(d1)
    for d in app.allDots:
        d.move(app.width, app.height)
    #pass


def updatedCounter(app):
    app.counter += 1
    
def redrawAll(app, canvas): #The View
    
    canvas.create_text(app.width//2,app.height//2,text=f"{int(app.counter//app.secondsDelay)}",font="Arial 100")
    for adot in app.allDots:
        
        adot.draw(canvas)

runApp(width=600, height=400)
