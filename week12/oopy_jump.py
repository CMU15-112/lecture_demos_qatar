from cmu_graphics import *
import random

class Sprite:
    
    def __init__(self, x, y):
        self.r = 25
        self.x = x
        self.y = y - self.r
        self.dx = 0
        self.dy = 0
        self.ddy = 1
        self.color = "black"
        
    def draw(self, app):
        drawCircle(self.x, self.y, self.r, fill=self.color)
        
    def onStep(self, app):
        self.x += self.dx
        self.dy += self.ddy
        self.y += self.dy
        
        if self.y + self.r > app.groundHeight:
            self.y = app.groundHeight - self.r
            self.dy = 0
            
    def onGround(self, app):
        return self.y + self.r == app.groundHeight
    
    def checkCollision(self, other):
        d = distance(self.x, self.y, other.x, other.y)
        if d <= self.r + other.r:
            return True
        else:
            return False
    
    def getAngle(self, other):
        return angleTo(self.x, self.y, other.x, other.y)

class Hero(Sprite):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.color = "red"

class Walker(Sprite):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.color = "purple"
        self.dx = -5

class Randomizer(Sprite):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.dx = -5
        self.color = "orange"
        self.blips = random.randint(0, 30)
        
    def onStep(self, app):
        self.blips += 1
        if self.blips % (app.stepsPerSecond) == 0:
            newdir = random.choice([1, -1])
            self.dx *= newdir
        
        super().onStep(app)

def reset(app):
    app.blips = 0
    app.groundHeight = 2 * app.height / 3
    app.bushR = 50
    
    app.hero = Hero(app.width/5, app.groundHeight)
    app.enemies = []
    app.enemies.append(Walker(4 * app.width / 5, 50))

# Controller
def onAppStart(app):
    reset(app)

# Controller
def onMousePress(app, x, y):
    pass

# Controller
def onKeyHold(app, keys):
    if "right" in keys:
        app.hero.x += 5
    if "left" in keys:
        app.hero.x -= 5
    if "up" in keys and app.hero.onGround(app):
        app.hero.dy = -15
 
# View
def redrawAll(app):
    
    for b in range(app.bushR, app.width + app.bushR, 2 * app.bushR):
        drawCircle(b, app.groundHeight, app.bushR, fill="green")
    
    drawRect(0, app.groundHeight, app.width, app.height - app.groundHeight, fill="brown")
    
    app.hero.draw(app)
    
    for e in app.enemies:
        e.draw(app)

# Controller
def onStep(app):
    app.blips += 1
    
    if app.blips % (4 * app.stepsPerSecond) == 0:
        app.enemies.append(Walker(4 * app.width / 5, 50))
    elif app.blips % (2 * app.stepsPerSecond) == 0:
        app.enemies.append(Randomizer(app.width//2, 50))
    
    app.hero.onStep(app)
    
    for e in app.enemies:
        e.onStep(app)
        if app.hero.checkCollision(e):
            a = app.hero.getAngle(e)
            if a > 180-45 and a < 180+45:
                # Hero wins, enemy dies
                pass
            else:
                # Enemy wins, hero dies
                pass

runApp(width=800, height=600)