from cmu_112_graphics import *
# every mouse pressed, draw a green dot, 20 px radius, at the position of
# the mouse pressed
# when an existing dot gets a click, it is removed

def appStarted(app):
    app.counter = 0
    app.dots = []
    app.r = 10


def distance(x1,y1, x2,y2):
    return ((x1 - x2)**2 + (y1 - y2)**2)**0.5
        

def mousePressed(app, event):
    ignore = False
    for (x,y) in app.dots:
        if distance(x,y, event.x, event.y) < 20:
            ignore = True
    if ignore == False:
        app.dots.append((event.x, event.y))
        return
    
    # if delete 
    for (x,y) in app.dots:
        if distance(x,y, event.x, event.y) < 10:
            app.dots.remove((x,y))
    
def redrawAll(app, canvas):
    for dot in app.dots:
        canvas.create_oval(dot[0]-app.r, dot[1]-app.r,
                       dot[0]+app.r, dot[1]+app.r,
                       fill='darkGreen')
  
runApp(width=800, height=600)