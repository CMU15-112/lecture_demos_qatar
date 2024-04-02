from cmu_graphics import *
from cmu_graphics.shape_logic import loadImageFromStringReference

class Hero(object):
    
    def __init__(self, x, y):
        self.r = 25
        self.x = x
        self.y = y-self.r
        self.color = "red"
        self.isDead = False
        
        self.dy = 0
        self.ddy = 1
    
    def draw(self, app):
        drawCircle(self.x - app.scrollX, self.y, self.r, fill=self.color)
        
    def onStep(self, app):
        self.y += self.dy
        self.dy += self.ddy

        if not self.isDead and self.y + self.r >= app.groundLevel and self.x > 0 and self.x < app.groundWidth:
            self.dy = 0
            self.y = app.groundLevel - self.r

    def kill(self):
        self.isDead = True
        self.color = "black"
        
class Goomba(object):
    
    images = [loadImageFromStringReference("goomba1-smaller.png"),
              loadImageFromStringReference("goomba2-smaller.png")]
    def __init__(self, x, y):
        self.w, self.h = getImageSize(Goomba.images[0])
        self.x = x
        self.y = y - self.h//2
        self.dy = 0
        self.ddy = 1
        self.dx = -5
        self.curImg = 0
        self.blips = 0
        self.isDead = False
        
    def draw(self, app):
        drawImage(Goomba.images[self.curImg], self.x - app.scrollX, self.y, align="center")

    def onStep(self, app):
        self.blips += 1
        if self.blips % 10 == 0:
            self.curImg = (self.curImg + 1) % 2

        self.x += self.dx
        
        self.y += self.dy
        self.dy += self.ddy
        
        if not self.isDead and self.y + self.h // 2 >= app.groundLevel and self.x > 0 and self.x < app.groundWidth:
            self.dy = 0
            self.y = app.groundLevel - self.h // 2
            
    def collidesWithHero(self, hero):
        if self.isDead:
            return False
        
        d = distance(self.x, self.y, hero.x, hero.y)
        if d < hero.r + self.w/2:
            return True
        else:
            return False
    
    def angleToHero(self, hero):
        return angleTo(self.x, self.y, hero.x, hero.y)
    
    def kill(self, app):
        self.isDead = True
        self.dx = 0
        #app.goombas.remove(self)

def reset(app):
    app.groundLevel = 2 * app.height / 3
    app.groundWidth = 2 * app.width
    
    app.bushR = 50
    
    app.scrollX = 0
    
    app.hero = Hero(100, app.groundLevel)
    
    app.goombas = []
    app.goombas.append(Goomba(700, app.groundLevel))
    app.goombas.append(Goomba(900, app.groundLevel))
    app.goombas.append(Goomba(1200, app.groundLevel))
    
    app.blips = 0

# This is called when the program starts
def onAppStart(app):
    reset(app)

# This is called every time one key is pressed
def onKeyHold(app, keys):
    
    if not app.hero.isDead:
        if "right" in keys:
            if app.hero.x - app.scrollX > 600:
                app.scrollX += 10
            app.hero.x += 10
        elif "left" in keys:
            if app.hero.x - app.scrollX < 200:
                app.scrollX -= 10
            app.hero.x -= 10
        
        if "up" in keys and app.hero.y == app.groundLevel - app.hero.r:
            app.hero.dy = -15

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
    app.blips += 1
    
    # Process the hero
    app.hero.onStep(app)
    
    # Add new goombas
    #if app.blips % 60 == 0:
    #    app.goombas.append(Goomba(app.groundWidth - 50, 0))
    
    # Process each Goomba and look for collisions with the hero
    for g in app.goombas[:]:
        g.onStep(app)
        if g.collidesWithHero(app.hero):
            a = g.angleToHero(app.hero)
            if a > 315 or a < 45:
                g.kill(app)
            else:
                app.hero.kill()
        if g.y > app.height:
            # A goomba should die
            g.kill(app)
            app.goombas.remove(g)
            # Now, spawn a new Goomba
            app.goombas.append(Goomba(app.groundWidth - 50, 0))

# This is how you run the program
runApp(width=800, height=600)

