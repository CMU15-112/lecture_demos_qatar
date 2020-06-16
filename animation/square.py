from cmu_112_graphics import *
import random


# appStarted happens when the program starts
# initialize model (variables) that belong to the model
def appStarted(app):
    app.number = 60 # number in the model
    app.timerDelay = 100
    app.box_y = app.height//2
    app.timerCount=0
    app.dir="down"
    app.showSquare = True
   
# for keyboard
def keyPressed(app, event):
    pass
   
# for mouse
def mousePressed(app, event):
    pass
            
# for time-based actions
def timerFired(app):
    app.timerCount+=1
    if app.timerCount%10==0:
        # once per second
        if app.showSquare==True:
            app.showSquare=False
        else:
            app.showSquare=True
        print(app.showSquare)
        app.number -= 1
        if app.number == 0:
            app.number = 60
    if app.dir=="up":
        app.box_y -= 3
    else:
        app.box_y += 3
    # update dir if needed
    if app.box_y  < 20:
        app.dir = "down"
    if app.box_y > app.height - 20:
        app.dir = "up"
   

# the main function for the view
# here you draw in the canvas (using the model app.xxxx)
def redrawAll(app, canvas):
    # centered
    # dimensions 40x40
    if app.showSquare==True:    
        canvas.create_rectangle(app.width//2 -20, app.box_y-20, app.width//2+20, app.box_y+20, fill="blue")
        canvas.create_text(app.width//2, app.box_y, text=str(app.number), fill="white")
   
runApp(width=400, height=400)