from cmu_112_graphics import *

def appStarted(app):
    app.cx = app.width//2
    app.cy = app.height//2
    app.r = 40
    
def mousePressed(app, event):
    app.cx = event.x
    app.cy = event.y
    
def redrawAll(app, canvas):
    canvas.create_text(app.width/2, 20,
                       text='Move dot with mouse presses',
                       fill='black')
    canvas.create_oval(app.cx-app.r, app.cy-app.r,
                       app.cx+app.r, app.cy+app.r,
                       fill='darkGreen')
runApp(width=400, height=400)