from cmu_graphics import *
import math
import random

# Controller Function: called ONCE when the app starts
def onAppStart(app):
    app.gameOver = False
    app.displayText = ''
    app.target= 42
    app.guesses = []
    
    # Controller Function: called presses with the mouse on the canvas
def onMousePress(app, x, y):
    if app.gameOver:
        return
    
    #square x : app.width - 50 -> app.width
    #square y: 0 -> 50
    if x >= app.width - 50 and y <= 50:
        app.displayText = "It's " + str(app.target)
    
    
            
# Controller Function: called when user pressed a key
def onKeyPress(app, key):
    if app.gameOver:
        return
    if key.isdigit():
        if not app.displayText.isdigit():
            app.displayText =''
            
        app.displayText+=key
    elif key == 'backspace' and app.displayText:
        app.displayText = app.displayText[:-1]
    elif key == 'enter':
        v = int(app.displayText)
        app.displayText =''
        
        if v in app.guesses:
            app.displayText = 'duplicate guess'
            return
        
        if v > app.target:
            app.displayText = 'go lower'
            app.guesses.append(v)
        elif v < app.target:
            app.displayText = 'go higher'
            app.guesses.append(v)
        else:
            app.gameOver = True

# This is the view - called after every controller function
def redrawAll(app):
    if not app.gameOver:
        drawRect(app.width-50, 0, 50 , 50, fill='green')
        drawLabel("cheat", app.width-25, 25)
        if app.displayText:# != ''
            drawLabel(app.displayText, app.width//2, app.height//2)
    else:
        drawLabel('You won', app.width//2, app.height//2)

runApp(width=600, height=600)



