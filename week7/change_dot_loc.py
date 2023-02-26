from cmu_112_graphics import *

def appStarted(app):
    app.cx = app.width//2
    app.cy = app.height//2
    app.r = 40
    app.colorList = ['red', 'blue', 'green', 'orange']
    app.colorIndex = 0
    
    
def mousePressed(app, event):
    app.cx = event.x
    app.cy = event.y
    app.colorIndex += 1
    app.colorIndex = app.colorIndex % 4
    
    
def redrawAll(app, canvas):
    canvas.create_text(app.width/2, 50,
                       text='Move dot with mouse',
                       fill='black',
                       font='Arial 25 bold')
    canvas.create_oval(app.cx-app.r, app.cy-app.r,
                       app.cx+app.r, app.cy+app.r,
                       fill=app.colorList[app.colorIndex])
runApp(width=800, height=800)