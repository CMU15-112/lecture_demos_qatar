from cmu_112_graphics import *
import random

class Dot(object):
    def __init__(self, x, y, r, color, dx, dy):
        self.x = x
        self.y = y
        self.r = r
        self.color = color
        self.dx = dx
        self.dy = dy
        
    def draw(self, app, canvas):
        canvas.create_oval(self.x-self.r,self.y-self.r,
                           self.x+self.r,self.y+self.r,
                           fill=self.color)
        
# This sets up the model
def appStarted(app):
    # Configuration
    app.timerDelay = 10
    app.speed = 10
    app.counter = 0
    r = random.randint(5, 20)
    color = random.choice(["red","yellow","blue","green"])
    x = random.randint(0, app.width)
    y = random.randint(0, app.height)
    dx = random.randint(-1, 1)
    dy = random.randint(-1, 1)
    app.speed = 1
    app.dot = Dot(x,y,r,color,dx,dy)
    app.gameState = "playing"
    
    

def timerFired(app):
    app.counter += 1
    
    app.dot.x += (app.speed * app.dot.dx)
    app.dot.y += (app.speed * app.dot.dy)
        
    if app.dot.x + app.dot.r > app.width or app.dot.x - app.dot.r < 0:
        app.dot.dx *= -1
    if app.dot.y + app.dot.r > app.height or app.dot.y - app.dot.r < 0:
        app.dot.dy *= -1
    
        

def mousePressed(app, event):
 
    d = ((event.x - app.dot.x)**2 + (event.y - app.dot.y)**2)**0.5
    if d <= app.dot.r:
        print("Game over")
        app.gameState = "gameOver"
            

# This is part of the controller
def keyPressed(app, event):
    if event.key == "Up":
        app.speed += 1
    if event.key == "Down":
        app.speed -= 1
        app.speed = max(1, app.speed)

# This is the view
def redrawAll(app, canvas):
    if app.gameState == "gameOver":
        canvas.create_rectangle(0,0,app.width, app.height, fill="blue")
        canvas.create_text(app.width//2, app.height//2, text="Game Over", fill="white", font="Arial 60 bold")
    else:
 
        app.dot.draw(app, canvas)
    

runApp(width=800, height=800)