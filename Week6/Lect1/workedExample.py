from cmu_graphics import *
import math
import random

'''
1) What shapes are drawn during gameplay? Describe their colors and arrangement
2) Under what condition are some shapes NOT drawn? When does the display change?
3) What properties change about each shape?
4) What triggers the changes (time-based or action-based)?
5) What exact condition must be met for the player to score a point?
    Point to the specific line of code.
6) What does the helper function do?
7) When does the game end?
8) What is displayed when the game ends? What is NOT displayed anymore, and why?
'''

def distance(x0, y0, x1, y1):
    return math.sqrt((x1-x0)**2 + (y1 - y0)**2)

def helper(app):
    app.cx = random.randint(app.r, app.width - app.r)
    app.cy = random.randint(app.r, app.height - app.r)

def reset(app):
    app.count = 0
    app.cx = app.width // 2
    app.cy = app.height // 2
    app.r = 200
    app.p = 0
    app.gameOver = False
    
# This is called when the program starts
def onAppStart(app):
    reset(app)

# This is called every time one key is pressed
def onKeyPress(app, key):
    if key in "rR":
        reset(app)

# This is called every time a mouse button is pressed
def onMousePress(app, x, y):
    if distance(app.cx, app.cy, x, y) < app.r/5:
        app.p += 1
        app.r -= 50
        if app.r <= 0:
            app.r = 1
            app.gameOver = True
        helper(app)

# This is called many times to refresh the window
def redrawAll(app):
    drawLabel(f"Points: {app.p} in {app.count/30:.2f} seconds", 
              app.width // 2, app.height // 30, size = app.width // 20)
    if app.gameOver == False:
        for i in range(5):
            if i % 2 == 0:
                color = 'red'
            else:
                color = 'white'
            r = app.r - (i * app.r / 5)
            drawCircle(app.cx, app.cy, r, fill = color)
    else:
        drawLabel(f"Game Over!  You win!", app.width // 2,
                  app.height // 2, size = app.width // 13)




# This is called "often" (def. by app.stepsPerSecond)
def onStep(app):
    if app.gameOver == False:
        app.count += 1

# This is how you run the program
runApp(width=800, height=800)