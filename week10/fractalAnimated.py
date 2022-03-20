from cmu_112_graphics import *


def appStarted(app):
    app.depth = 1
    app.maxCalls = 0
    app.ticks = 0
    app.autoplay = True
    
    
def drawTSquare(canvas, x, y, width, color, depth, calls=0, maxCalls=1000):
    if depth == 0:
        return calls
    if calls >= maxCalls:
        return calls
    canvas.create_rectangle(x - width //2, y - width //2, x + width//2, y + width//2, fill=color, width=1)
    next_width = width // 2
    calls += 1
    calls = drawTSquare(canvas, x - width //2, y - width //2, next_width, color, depth-1, calls, maxCalls)
    calls = drawTSquare(canvas, x - width //2, y + width //2, next_width, color, depth-1, calls ,maxCalls)
    calls = drawTSquare(canvas, x + width //2, y - width //2, next_width, color, depth-1, calls, maxCalls)
    calls = drawTSquare(canvas, x + width //2, y + width //2, next_width, color, depth-1, calls, maxCalls)
    return calls
 
def timerFired(app):
    app.ticks += 1
    if app.ticks % 2 == 0 and app.autoplay:
        app.maxCalls += 1
 
def keyPressed(app, event):
    if event.key == "Up":
        app.depth += 1
        app.maxCalls = 0
    if event.key == "Right":
        app.maxCalls += 1
    if event.key == "Left":
        app.maxCalls -= 1
    if event.key == "r" or event.key == "R":
        app.maxCalls = 0
    #print("keyPressed", app.depth, app.maxCalls)

def redrawAll(app, canvas):
    canvas.create_text(10, 10, text=f"max depth={app.depth}",  anchor='nw', font="Arial 20")
    canvas.create_text(10, 90, text=f"max calls ={app.maxCalls}",  anchor='nw', font="Arial 20")
    calls = drawTSquare(canvas, app.width//2, app.height//2, 200, 'blue', app.depth, 0, app.maxCalls)        

runApp(width=800, height=800)