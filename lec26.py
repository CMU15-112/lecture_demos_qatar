from cmu_112_graphics import *
import random
class dot():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.color =  random.choice(["red","blue","green","pink","yellow","purple","orange","brown"])
        self.r = random.randint(5,10)
        self.dx = random.randint(-20,20)
        self.dy = random.randint(-20,20)
    def draw(self,canvas,app):
        if self.x > (app.Xref - app.width//2) and self.x < (app.Xref + app.width//2):
            canvas.create_oval((self.x-self.r)-(app.Xref - app.width//2),self.y-self.r,(self.x+self.r)-(app.Xref - app.width//2),self.y+self.r,fill=self.color)
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
    app.worldWidth = 2000
    app.Xref = 500
    
    #pass

def keyPressed(app,e):
    if e.key == "Left":
        if (app.Xref > app.width//2): 
            app.Xref -= 20
    elif e.key == "Right":
        if (app.Xref < app.worldWidth - app.width//2):
            app.Xref += 20

def timerFired(app): # The Controller
    #app.counter = app.counter + 1
    updatedCounter(app)
    #if app.counter == 500:
    #    app.timerRunning = False
    if app.counter %5 == 0:
        d1 = dot(random.randint(1,app.worldWidth),random.randint(1,app.height))
        app.allDots.append(d1)
    for d in app.allDots:
        d.move(app.worldWidth, app.height)
    #pass


def updatedCounter(app):
    app.counter += 1
    
def redrawAll(app, canvas): #The View
    
    #canvas.create_text(app.width//2,app.height//2,text=f"{int(app.counter//app.secondsDelay)}",font="Arial 100")
    for adot in app.allDots:
        adot.draw(canvas,app)

runApp(width=600, height=400)
