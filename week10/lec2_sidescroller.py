from cmu_112_graphics import *

def appStarted(app):
    app.groundLevel = app.height * 2 / 3
    app.bushR = 50
    
    app.heroR = 20
    app.heroX = 250
    app.heroY = app.groundLevel-app.heroR
    
    app.dy = 0
    app.ddy = 1
    
    app.scrollX = 0

def timerFired(app):
    app.heroY += app.dy
    app.dy += app.ddy
    
    if app.heroY+app.heroR >= app.groundLevel and app.heroX > 0 and app.heroX < 2*app.width:
        app.dy = 0
        app.heroY = app.groundLevel-app.heroR

def keyPressed(app, event):
    if event.key == "Right":
        if app.heroX - app.scrollX > 800:
            app.scrollX += 10
        app.heroX += 10
    elif event.key == "Left":
        if app.heroX-app.scrollX < 200:
            app.scrollX -= 10
        app.heroX -= 10
    elif event.key == "Up":
        app.dy = -15
    elif event.key == "d":
        app.scrollX += 25
    elif event.key == "a":
        app.scrollX -= 25
        
    

def redrawAll(app, canvas):
    # Draw the bushes
    for bushLeft in range(0, 2*app.width, 2*app.bushR):
        canvas.create_oval(bushLeft-app.scrollX, app.groundLevel-app.bushR,
                           bushLeft+2*app.bushR-app.scrollX, app.groundLevel+app.bushR,
                           fill="green")

    # The ground
    canvas.create_rectangle(0-app.scrollX, app.groundLevel, 2*app.width-app.scrollX, app.height,
                            fill="brown")
    
    # The hero
    canvas.create_oval(app.heroX-app.heroR-app.scrollX, app.heroY-app.heroR,
                       app.heroX+app.heroR-app.scrollX, app.heroY+app.heroR,
                       fill = "red")
    

runApp(width=1000, height=500)