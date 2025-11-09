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
        self.dead = False
        
    def draw(self, app):
        drawCircle(self.x - app.scrollX, self.y, self.r, fill=self.color)
        
    def onStep(self, app):
        self.x += self.dx
        self.dy += self.ddy
        self.y += self.dy
        
        if not self.dead and self.y + self.r > app.groundHeight:
            self.y = app.groundHeight - self.r
            self.dy = 0
            
    def onGround(self, app):
        return self.y + self.r == app.groundHeight
    
    def checkCollision(self, other):
        if other.dead:
            return False
        
        d = distance(self.x, self.y, other.x, other.y)
        if d <= self.r + other.r:
            return True
        else:
            return False
    
    def getAngle(self, other):
        return angleTo(self.x, self.y, other.x, other.y)
    
    def isOffScreen(self, app):
        if self.x + self.r < 0 or \
           self.x - self.r > app.levelWidth or \
           self.y - self.r > app.height:
            return True
        return False

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
        
class Goomba(Walker):
    images = ["goomba1-smaller.png", "goomba2-smaller.png"]
    
    def __init__(self, x, y):
        super().__init__(x, y)
        self.curImg = 0
        self.w, self.h = getImageSize(Goomba.images[self.curImg])
        self.r = self.w / 2
        
    def draw(self, app):
        drawImage(Goomba.images[self.curImg], self.x - app.scrollX,
                  self.y, align="center")
        
    def onStep(self, app):
        super().onStep(app)
        if app.blips % (app.stepsPerSecond // 6) == 0:
            self.curImg = (self.curImg + 1) % 2
        

def reset(app):
    app.blips = 0
    app.groundHeight = 2 * app.height / 3
    app.bushR = 50
    app.gameOver = False
    
    app.levelWidth = 2000
    app.scrollX = 0
    
    app.hero = Hero(app.width/5, app.groundHeight)
    app.enemies = []
    app.enemies.append(Goomba(4 * app.width / 5, 50))

# Controller
def onAppStart(app):
    reset(app)

# Controller
def onMousePress(app, x, y):
    pass

# Controller
def onKeyHold(app, keys):
    if "r" in keys:
        reset(app)
        return
    
    if app.gameOver:
        return
    
    if "d" in keys:
        app.scrollX += 5
    if "a" in keys:
        app.scrollX -= 5
    
    if "right" in keys:
        app.hero.x += 5
        if app.hero.x - app.scrollX > 0.8 * app.width:
            app.scrollX += 5
        print(app.hero.x)
    if "left" in keys:
        app.hero.x -= 5
        if app.hero.x - app.scrollX < app.width * 0.2:
            app.scrollX -= 5
    if "up" in keys and app.hero.onGround(app):
        app.hero.dy = -15
 
# View
def redrawAll(app):
    if app.gameOver:
        drawLabel("Game Over", app.width/2, 100)
    
    for b in range(app.bushR, app.levelWidth, 2 * app.bushR):
        drawCircle(b-app.scrollX, app.groundHeight, app.bushR, fill="green")
    
    drawRect(0, app.groundHeight, app.width, app.height - app.groundHeight, fill="brown")
    
    app.hero.draw(app)
    
    for e in app.enemies:
        e.draw(app)

# Controller
def onStep(app):
    if app.gameOver:
        return
    
    app.blips += 1
    
    if app.blips % (4 * app.stepsPerSecond) == 0:
        app.enemies.append(Goomba(3 * app.levelWidth / 4, 50))
    elif app.blips % (2 * app.stepsPerSecond) == 0:
        app.enemies.append(Randomizer(app.levelWidth//2, 50))
    
    app.hero.onStep(app)
    
    for e in app.enemies[:]:
        e.onStep(app)
        if e.isOffScreen(app):
            app.enemies.remove(e)
            print(f"killed an enemy {e}")
            continue
        if app.hero.checkCollision(e):
            a = app.hero.getAngle(e)
            if a > 180-45 and a < 180+45:
                # Hero wins, enemy dies
                e.dead = True
            else:
                # Enemy wins, hero dies
                app.hero.dead = True
    
    if app.hero.isOffScreen(app):
        app.gameOver = True

runApp(width=800, height=600)