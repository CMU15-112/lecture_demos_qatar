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
def initGame(app):
    r = random.randint( 20, 50)  # choose a random radius
    color = random.choice(["red","yellow","blue","green"])  # choose a random color
    x = random.randint(r, app.width - r)  # choose a random starting loc
    y = random.randint(r, app.height -r)
    dx = 0
    dy = 0
    dirs = [-1, 1]
    dx = dirs[random.randint(0, 1)]  # choose a random direction on the x-axis: -1 or 1
    dy = dirs[random.randint(0, 1)]  # choose a random direction on the y-axis: -1 or 1
    app.dot = Dot(x,y,r,color,dx,dy)  # create the dot
    app.countDown = 10  # countdown timer in seconds
    app.gameState = "playing"  # game state variable
    app.blinking = False  # blinking active or not
    app.blinkState = False # when blinking is active, to draw or not to draw

def appStarted(app):
    # Configuration
    app.timerDelay = 50  # 50 ms = 1000/50 = 20 updates per second
    app.speed = 10        # speed of the dot in pixels per update
    app.counter = 0      # used to count how many updates have been made
    initGame(app)  # helper function to define game variables
    
    

def timerFired(app):
    app.counter += 1 
    if app.counter % 20 == 0:  # every 20 counter increments (1 second)
        if app.gameState == "playing":  # only decremement when playing
            app.countDown -= 1
            if app.countDown <= 5:  # blink the last 5 seconds
                app.blinking = True
            if app.countDown == 0:  # game over
                app.gameState = "gameOver"
    
    if app.counter % 10 == 0:  # every 10 counter increments (0.5 second)
        if app.gameState == "playing" and app.blinking:  # in state playing and blinking is active
            app.blinkState = not app.blinkState  # flag to know whether the dot is shown or not
                                                 # during blinking state
    
    # only move when playing
    if app.gameState == "playing":
        # update dot position based on the direction and "speed"
        app.dot.x += (app.speed * app.dot.dx)
        app.dot.y += (app.speed * app.dot.dy)
            
        # bounce: when the dot touches the side edges (left, right)
        # change dx direction
        if app.dot.x + app.dot.r > app.width or app.dot.x - app.dot.r < 0:
            app.dot.dx *= -1
        # bounce: when the dot touches the side edges (top, bottom)
        # change dy direction
        if app.dot.y + app.dot.r > app.height or app.dot.y - app.dot.r < 0:
            app.dot.dy *= -1

def mousePressed(app, event):
 
    d = ((event.x - app.dot.x)**2 + (event.y - app.dot.y)**2)**0.5
    if d <= app.dot.r:
        app.gameState = "win"
        
# This is part of the controller
def keyPressed(app, event):
    if event.key == "Up":
        app.speed += 1
    if event.key == "Down":
        app.speed -= 1
        app.speed = max(1, app.speed)
    if event.key == 'r':
        if app.gameState == "win" or app.gameState == "gameOver":
            initGame(app)  # restart the game
            app.gameState = "playing"
    if event.key == "p":  # pause/unpause the game
        if app.gameState == "playing":
            app.gameState = "pause"
        else:
            app.gameState = "playing"
    if event.key == "b":  # toggle blinking 
        if app.gameState == "playing":
            app.blinking = not app.blinking  
        

# This is the view
def redrawAll(app, canvas):
    if app.gameState == "gameOver":
        canvas.create_rectangle(0,0,app.width, app.height, fill="blue")
        canvas.create_text(app.width//2, app.height//2, text="Game Over", fill="white", font="Arial 60 bold")
    elif app.gameState == "win":
        canvas.create_rectangle(0,0,app.width, app.height, fill="blue")
        canvas.create_text(app.width//2, app.height//2, text="You Won", fill="white", font="Arial 60 bold")

    elif app.gameState == "pause":
        canvas.create_rectangle(0,0,app.width, app.height, fill="blue")
        canvas.create_text(app.width//2, app.height//2, text="Pause", fill="white", font="Arial 60 bold")
    else:  # playing
        canvas.create_text(app.width, app.height, text=f"Time Remaining: {app.countDown}",
                           font="Arial 20 bold", anchor='se')
        if app.blinking:  # blinking active, only draw when blinkState is True
            if app.blinkState:
                app.dot.draw(app, canvas)
        else:  # blinking inactive, draw always
            app.dot.draw(app, canvas)
    

runApp(width=1000, height=1000)