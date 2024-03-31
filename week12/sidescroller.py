from cmu_graphics import *

class Hero(object):
    
    def __init__(self, x, y):
        self.r = 25
        self.x = x
        self.y = y-self.r
        self.color = "red"
        
        self.dy = 0
        self.ddy = 1
    
    def draw(self, app):
        drawCircle(self.x - app.scrollX, self.y, self.r, fill=self.color)
        
    def onStep(self, app):
        if self.y + self.r > app.groundLevel and self.x > 0 and self.x < app.groundWidth:
            self.dy = 0
            self.y = app.groundLevel - self.r

        self.y += self.dy
        self.dy += self.ddy
        

class Goomba(object):
    
    images = ["goomba1-smaller.png", "goomba2-smaller.png"]
    def __init__(self, x, y):
        self.w, self.h = getImageSize(Goomba.images[0])
        self.x = x
        self.y = y - self.h//2
        self.curImg = 0
        self.blips = 0
        
    def draw(self, app):
        drawImage(Goomba.images[self.curImg], self.x - app.scrollX, self.y, align="center")
        
    def onStep(self, app):
        self.blips += 1
        if self.blips % 10 == 0:
            self.curImg = (self.curImg + 1) % 2

        self.x -= 5

def reset(app):
    app.groundLevel = 2 * app.height / 3
    app.groundWidth = 2 * app.width
    
    app.bushR = 50
    
    app.scrollX = 0
    
    app.hero = Hero(100, app.groundLevel)
    
    app.goombas = []
    app.goombas.append(Goomba(700, app.groundLevel))

# This is called when the program starts
def onAppStart(app):
    reset(app)

# This is called every time one key is pressed
def onKeyHold(app, keys):
    
    if "right" in keys:
        if app.hero.x - app.scrollX > 600:
            app.scrollX += 10
        app.hero.x += 10
    elif "left" in keys:
        if app.hero.x - app.scrollX < 200:
            app.scrollX -= 10
        app.hero.x -= 10
    
    print(app.hero.dy)
    if "up" in keys and app.hero.dy == 1:
        app.hero.dy = -20
    
    if "d" in keys:
        app.scrollX += 10
    elif "a" in keys:
        app.scrollX -= 10
        
    if "r" in keys:
        reset(app)

# This is called every time a mouse button is pressed
def onMousePress(app, x, y):
    pass

# This is called many times to refresh the window
def redrawAll(app):
    
    for bushLeft in range(0, app.groundWidth, 2*app.bushR):
        drawCircle(bushLeft-app.scrollX, app.groundLevel, app.bushR, fill="green")
    
    drawRect(0-app.scrollX, app.groundLevel, app.groundWidth, app.height / 3, fill="brown")
    
    app.hero.draw(app)
    
    for g in app.goombas:
        g.draw(app)

# This is called "often" (def. by app.stepsPerSecond)
def onStep(app):
    app.hero.onStep(app)
    
    for g in app.goombas:
        g.onStep(app)

# This is how you run the program
runApp(width=800, height=600)

