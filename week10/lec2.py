from cmu_112_graphics import *

def appStarted(app):
    app.groundLevel = 2 * app.height / 3
    app.bushWidth = 100
    
    # X and Y are the center of the hero
    app.heroRadius = 15
    app.heroX = app.heroRadius+100
    app.heroY = app.groundLevel-app.heroRadius
    
    # Upward speed of the character
    app.dy = 0
    
    # Gravity
    app.ddy = 1
    
    # Define the level width
    app.levelWidth = int(app.width * 1.5)
    
    app.scrollX = 0

def timerFired(app):
    app.heroY -= app.dy
    #if app.dy > 0:
    app.dy -= app.ddy
    
    if app.heroY+app.heroRadius >= app.groundLevel and \
    app.heroX > -app.heroRadius and app.heroX < app.levelWidth:
        app.dy = 0
        app.heroY = app.groundLevel - app.heroRadius

def keyPressed(app, event):
    if event.key == "Right":
        app.heroX += 10
    elif event.key == "Left":
        app.heroX -= 10
    elif event.key == "a":
        app.scrollX -= 10
    elif event.key == "d":
        app.scrollX += 10
    elif event.key == "Up":
        app.dy = 15
        
    # Detect when hero is close to the screen
    heroLoc = app.heroX - app.scrollX
    if heroLoc >= app.width-100:
        app.scrollX += 10
    elif heroLoc <= 100:
        app.scrollX -= 10
        

def redrawAll(app, canvas):
    for bushLeft in range(0, app.levelWidth, app.bushWidth):
        bushLeft -= app.scrollX
        canvas.create_oval(bushLeft, app.groundLevel - app.bushWidth/2,
                           bushLeft+app.bushWidth,
                           app.groundLevel + app.bushWidth/2,
                           fill = "green")
        
    canvas.create_rectangle(0-app.scrollX, app.groundLevel,
                            app.levelWidth - app.scrollX,
                            app.height, fill="brown")
    
    heroLoc = app.heroX - app.scrollX
    canvas.create_oval(heroLoc - app.heroRadius,
                       app.heroY - app.heroRadius,
                       heroLoc + app.heroRadius,
                       app.heroY + app.heroRadius,
                       fill="red")

runApp(width=800, height=400)