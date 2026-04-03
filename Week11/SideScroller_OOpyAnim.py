from cmu_graphics import *
import random

##################################### CLASSES #################################

class Cloud(object):
    
    def __init__(self, x, y):
        # the center coordinates of the first circle in the cloud
        self.x = x
        self.y = y
        #dx captures speed and direction
            # the cloud moves (2) pixels/step
            # (-) means it moves to the left
        self.dx = -2 
    
    
    #drawn as three overalaping circles.
    def draw(self):
        drawCircle(self.x, self.y, 18, fill='white') #main circle
        drawCircle(self.x + 18, self.y, 22, fill='white')
        drawCircle(self.x + 36, self.y, 18, fill='white')        

    # We call this in onStep(), to move the shape
        # 
    def update(self):
        self.x += self.dx #decrease x by 2 
        if self.x < -60: #whole cloud gets off screen
            self.x = 860 # reposition to show up at the right side
            self.y = random.randint(40, 140)
   
   
class Player(object):
    
    def __init__(self, x, groundY):
        
        self.groundY = groundY
        #dimensions of the rectangle shape
        self.width = 40
        self.height = 60
        #top-left corner coordinates for the rectangle shape
        self.x = x
        self.y = self.groundY-self.height
        self.dy = 0
        self.gravity = 1
        self.onGround = True
        
    def draw(self):
        # The rectangle is the main shape,
            #other shapes are drawn relative to that shape
        drawRect(self.x, self.y, self.width, self.height, fill='dodgerBlue')
        drawCircle(self.x + 28, self.y + 18, 4, fill='white')
        drawCircle(self.x + 29, self.y + 18, 2, fill='black')
        drawLine(self.x + 10, self.y + self.height,
                 self.x + 10, self.y + self.height + 12, lineWidth=4)
        drawLine(self.x + 30, self.y + self.height,
                 self.x + 30, self.y + self.height + 12, lineWidth=4)
        
    def jump(self):
        if self.onGround:
            self.dy = -16
            self.onGround = False
            
    def update(self):
        if self.onGround == False:
            self.y += self.dy
            self.dy+= self.gravity
            
            if self.y +self.height >= self.groundY:
                self.y = self.groundY-self.height
                self.dy = 0
                self.onGround = True
    def getBounds(self):
        return (self.x, self.y, self.width,self.height)

class Obstacle(object):
    
    def __init__(self, x, groundY, scrollSpeed):
        self.width = random.choice([25, 30, 35])
        self.height = random.choice([35, 45, 55])
        self.groundY = groundY
        # top-left corner coordinates of the rectangle
        self.x = x
        self.y = self.groundY - self.height
        self.dx= -scrollSpeed #speed and direction
        
        
    def draw(self):
        drawRect(self.x, self.y, self.width, self.height, fill='crimson')
        drawLine(self.x, self.y, self.x + self.width, self.y, fill='black')
        
        
    def update(self):
        self.x+=self.dx
        
    def getBounds(self):
        return (self.x, self.y, self.width,self.height)
        
class Game(object):
    
    @staticmethod
    def updateObstacles(app):
        
        kept=[] #new list stores current obstacles 
        for o in app.obstacles:
            o.update()
            
            #offscreen
            if o.x+o.width <=0:
                app.score+=1
            else:
                kept.append(o)
        
        app.obstacles= kept
        
    @staticmethod
    def detectCollision(player, obstacle):
        px,py,pw,ph = player.getBounds()
        ox, oy, ow,oh =obstacle.getBounds()
        
        return (px< ox+ow and
                px+pw > ox and
                py < oy+oh and
                py+ph > oy)
    
    @staticmethod
    def updateDifficulty(app):
        if app.steps%120 ==0:
            app.scrollSpeed += 0.15
        
        if app.steps%180 == 0 and app.spawnDelay > 25:
            app.spawDelay -= 1

############################ CMU_GRAPHICS MAIN CODE ###########################


def onAppStart(app):
    app.groundY = 320
    resetGame(app)
    
def resetGame(app):
    app.gameOver = False
    app.clouds = [Cloud(120, 80), Cloud(420, 120), Cloud(700, 60)]
    app.player = Player(90, app.groundY)
    app.obstacles = []
    app.score= 0
    app.spawnDelay = 45 #steps to wait beforeadding new obstacle
    app.steps =0
    app.scrollSpeed = 6
    
def onKeyPress(app, key):
    if key in ['up','space']:
        app.player.jump()
    elif key in 'rR':
        resetGame(app)
        
#by default this is called 30 times/sec
def onStep(app):
    
    if app.gameOver:
        return
    
    app.steps+=1
    app.player.update()
    
    for c in app.clouds:
        c.update()
        
    Game.updateObstacles(app)
    
    if app.steps%app.spawnDelay==0:
        app.obstacles.append(Obstacle(app.width, app.groundY, app.scrollSpeed))
    
    for o in app.obstacles:
        if Game.detectCollision(app.player, o):
            app.gameOver= True
    
def redrawAll(app):
    # Sky
    drawRect(0,0, app.width, app.height, fill='skyBlue') 
    
    # ground
    drawRect(0, app.groundY, app.width, app.height-app.groundY, fill='lightGreen')
    drawLine(0, app.groundY, app.width, app.groundY, lineWidth = 3)
    
    
    drawLabel(f'Score: {app.score}', 70, 30, size=24, bold=True)
    
    #Clouds
    for c in app.clouds:
        c.draw()

    
    #Obstacles
    for o in app.obstacles:
        o.draw()
        
    #Player
    app.player.draw()
    
    if not app.gameOver:
        drawLabel('Press space to jump', app.width - 140, 30, size=18)
    else:
        drawRect(170, 110, 460, 140, fill='white', border='black')
        drawLabel('Game Over!', app.width/2, 150, size=32, bold=True, fill='crimson')
        drawLabel(f'Final Score: {app.score}', app.width/2, 190, size=22)
        drawLabel('Press r to restart', app.width/2, 225, size=20)


    
    
def main():
    runApp(width=800, height=400)


main()