from cmu_112_graphics import *
import random

###############################################################################
# Basic Moving Square Animation + Random Circles
###############################################################################
# LEARNING OBJECTIVES
# What is MVC?
# How do we use data to track variables in an animation?
# How does timerFired work?

# Worked example:
# read the specification, or see the result
# design the model data
# think about the view ( how data will be displayed?)
# identify the "controller" part or MVC. Keyboard, timer, mouse, etc?
# think about how data will change (from the controller side)


# timer, keyboard

# model (app)
def appStarted(app):
    # the number of milliseconds between calls to timerFired
    app.timerDelay = 20
    
    # position
    # initially center of canvas
    app.squareX = app.width//2
    app.squareY = app.height//2
    
    # size
    app.squareSize = 20
    
    # 1 pixel up, 1 pixel right
    # direction
    app.dx = 1
    app.dy = 1


# controller
# every 20 milliseconds
def timerFired(app):
    app.squareX += app.dx
    app.squareY += app.dy
    
    if (app.squareY+app.squareSize//2) >= app.height:
        app.dy *= -1
    elif (app.squareX+app.squareSize//2) >= app.width:
        app.dx *= -1
    elif (app.squareY-app.squareSize//2) <= 0:
        app.dy *= -1
    elif (app.squareX-app.squareSize//2) <= 0:
        app.dx *= -1


# called every time the window changes size
def sizeChanged(app):
    print("sizeChanged event")
# controller

# presses the keyboard
# only update model (position, size, direction)
# if you want to get key presses
def keyPressed(app, event):
    print("Key pressed")
    app.squareY -= 5
    app.squareX -= 5
    """
    if event.key == "Left":
        app.squareX -= 5
    elif event.key == "Right":
        app.squareX += 5
    elif event.key == "Up":
        app.squareY -= 5
    elif event.key == "Down":
        app.squareY += 5
"""
# view
def redrawAll(app, canvas):
   
    # draw the square at its current position
    # draw square
    canvas.create_rectangle(app.squareX-app.squareSize//2,
                            app.squareY-app.squareSize//2,
                            app.squareX+app.squareSize//2,
                            app.squareY+app.squareSize//2,
                            fill="blue") 
    

runApp(width=800, height=400)