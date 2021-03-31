from cmu_112_graphics import *
import random

def distance(x1, y1, x2, y2):
    d = ((x2-x1)**2 + (y2-y1)**2)**0.5
    return d

def circlesIntersect(x1, y1, r1, x2, y2, r2):
    d = distance(x1,y1,x2,y2)
    if d > r1+r2:
        return False
    else:
        return True

class Circle(object):
    def __init__(self, x, y, r, color, app, dx=5, dy=5):
        self.cx = x
        self.cy = y
        self.r = r
        self.color = color
        self.app = app
        self.dx = dx
        self.dy = dy
        
    def draw(self, canvas):
        canvas.create_oval(self.cx-self.r,self.cy-self.r,
                       self.cx+self.r,self.cy+self.r,fill=self.color)
        
    def moveCircle(self):
        self.cx += self.dx
        self.cy += self.dy
        
        circleRe = self.cx + self.r
        circleLe = self.cx - self.r    
        if circleRe >= self.app.width or circleLe <= 0:
            self.dx *= -1
            
        circleUe = self.cy - self.r
        circleDe = self.cy + self.r
        if circleUe <= 0 or circleDe >= self.app.height:
            self.dy *= -1        

# Setup the variables in the model
# Does not draw anything. (EVER)
def appStarted(app):
#     app.cx = app.width/2
#     app.cy = app.height/2
#     app.r = 80    
#     app.dx = 10
#     app.dy = 15

    app.timerDelay = 25

    app.circles = []
#     c = Circle(app.width/2, app.height/2, 80, "red", app, 4, 6)
#     app.circles.append(c)
#     c = Circle(40, 65, 40, "blue", app, 4, 2)
#     app.circles.append(c)

    colors = ["red", "blue", "green"]
    for i in range(25):
        r = random.randint(10,50)
        x = random.randint(r, app.width-r)
        y = random.randint(r, app.height-r)
        color = random.choice(colors)
        dx = random.randint(1,10)
        dy = random.randint(1,10)
        c = Circle(x, y, r, color, app, dx, dy)
        app.circles.append(c)
        

def timerFired(app):
    for circle in app.circles:
        circle.moveCircle()
        
    for i in range(len(app.circles)):
        for j in range(i,len(app.circles)):
            c1 = app.circles[i]
            c2 = app.circles[j]
            
            if circlesIntersect(c1.cx, c1.cy, c1.r, c2.cx, c2.cy, c2.r):
                c1.dx *= -1
                c1.dy *= -1
                c2.dx *= -1
                c2.dy *= -1

# Controller: Read/Write from the model.
#             Does not draw anything. (EVER)
def keyPressed(app, event):
    pass

# View: Draw the current view based on the model.
#       Does not change the model, EVER
def redrawAll(app, canvas):
    for circle in app.circles:
        circle.draw(canvas)

runApp(width=800, height=800)