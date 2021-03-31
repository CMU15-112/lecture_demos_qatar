from cmu_112_graphics import *

def appStarted(app):
    app.groundLevel = app.height * 2 / 3
    app.bushR = 50
    
    app.heroR = 20
    app.heroX = 50
    app.heroY = app.groundLevel-app.heroR

def keyPressed(app, event):
    if event.key == "Right":
        app.heroX += 5
    elif event.key == "Left":
        app.heroX -= 5

def redrawAll(app, canvas):
    # Draw the bushes
    for bushLeft in range(0, app.width, 2*app.bushR):
        canvas.create_oval(bushLeft, app.groundLevel-app.bushR,
                           bushLeft+2*app.bushR, app.groundLevel+app.bushR,
                           fill="green")

    # The ground
    canvas.create_rectangle(0, app.groundLevel, app.width, app.height,
                            fill="brown")
    
    # The hero
    canvas.create_oval(app.heroX-app.heroR, app.heroY-app.heroR,
                       app.heroX+app.heroR, app.heroY+app.heroR,
                       fill = "red")
    

runApp(width=1000, height=500)