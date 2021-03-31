from cmu_112_graphics import *

# Setup the variables in the model
# Does not draw anything. (EVER)
def appStarted(app):
    app.cx = app.width/2
    app.cy = app.height/2
    app.r = 80
    app.d = 4
    
    app.dx = 10
    app.dy = 15

# Handle mouse clicks
def mousePressed(app, event):
    app.cx = event.x
    app.cy = event.y

def timerFired(app):
    app.cx += app.dx
    app.cy += app.dy
    
    circleRe = app.cx + app.r
    circleLe = app.cx - app.r    
    if circleRe >= app.width or circleLe <= 0:
        app.dx *= -1
        
    circleUe = app.cy - app.r
    circleDe = app.cy + app.r
    if circleUe <= 0 or circleDe >= app.height:
        app.dy *= -1

# Controller: Read/Write from the model.
#             Does not draw anything. (EVER)
def keyPressed(app, event):
    print(event.key)
    if event.key == "Right" or event.key == "d":
        app.cx += app.d
    elif event.key == "Left" or event.key == "a":
        app.cx -= app.d
    elif event.key == "Up" or event.key == "w":
        app.cy -= app.d
    elif event.key == "Down" or event.key == "s":
        app.cy += app.d
    # Example for some diagonals
    elif event.key == "e":
        app.cx += app.d
        app.cy -= app.d
    elif event.key == "q":
        app.cx -= app.d
        app.cy -= app.d

# View: Draw the current view based on the model.
#       Does not change the model, EVER
def redrawAll(app, canvas):
    canvas.create_oval(app.cx-app.r,app.cy-app.r,
                       app.cx+app.r,app.cy+app.r,fill="red")

runApp(width=800, height=800)