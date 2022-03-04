from cmu_112_graphics import *
# every mouse pressed, draw a green dot, 20 px radius, at the position of
# the mouse pressed

def appStarted(app):
    app.counter = 0
    app.dots = []
    app.r = 20

def mousePressed(app, event):
    
    app.dots.append((event.x, event.y))
    
    
def redrawAll(app, canvas):
    for dot in app.dots:
        canvas.create_oval(dot[0]-app.r, dot[1]-app.r,
                       dot[0]+app.r, dot[1]+app.r,
                       fill='darkGreen')
  
runApp(width=800, height=600)