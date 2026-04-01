from cmu_graphics import *
import random

##################################### CLASSES #################################

class Cloud(object):
    
    def __init__(self, x, y):
        # the center coordinates of the first circle in the cloud
        self.x = x
        self.y = y
        #dx captures speed and direction
            # the cloud moves (2) pixels/update
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
        

class Obstacle(object):
    
    def __init__(self, x, groundY):
        self.width = random.choice([25, 30, 35])
        self.height = random.choice([35, 45, 55])
        self.groundY = groundY
        # top-left corner coordinates of the rectangle
        self.x = x
        self.y = self.groundY - self.height
        
        
    def draw(self):
        drawRect(self.x, self.y, self.width, self.height, fill='crimson')
        drawLine(self.x, self.y, self.x + self.width, self.y, fill='black')
        
############################ CMU_GRAPHICS MAIN CODE ###########################


def onAppStart(app):
    app.groundY = 320
    resetGame(app)
    
def resetGame(app):
    app.gameOver = False
    app.clouds = [Cloud(120, 80), Cloud(420, 120), Cloud(700, 60)]
    app.player = Player(90, app.groundY)
    app.obstacles = [Obstacle(350, app.groundY)]
    
#by default this is called 30 times/sec
def onStep(app):
    for c in app.clouds:
        c.update()
    
def redrawAll(app):
    # Sky
    drawRect(0,0, app.width, app.height, fill='skyBlue') 
    
    # ground
    drawRect(0, app.groundY, app.width, app.height-app.groundY, fill='lightGreen')
    drawLine(0, app.groundY, app.width, app.groundY, lineWidth = 3)
    
    #Clouds
    for c in app.clouds:
        c.draw()
    
    #Player
    app.player.draw()
    
    #Obstacles
    for o in app.obstacles:
        o.draw()
    
def main():
    runApp(width=800, height=400)


main()