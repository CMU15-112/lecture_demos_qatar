from cmu_112_graphics import *
import random

def randomPoint(app):
    x = random.randint(2*app.r, app.width-2*app.r)
    y = random.randint(2*app.r, app.height-2*app.r)
    return x, y


def appStarted(app):
    app.counter = 0
    app.r = 20
    app.cx, app.cy = randomPoint(app)


def mousePressed(app, event):
    if ((event.x - app.cx)**2 + (event.y - app.cy)**2)**0.5 < app.r:
        app.counter += 1

def keyPressed(app, event):
    if event.key == "Enter":
        app.counter = 0
        app.cx, app.cy = randomPoint()

def redrawAll(app, canvas):
    canvas.create_text(app.width/2, 100,
                       text=f'{app.counter}',
                       font='Arial 30 bold',
                       fill='black')

    for i in range(5):
        if i%2 == 0:
            color = 'black'
        else:
            color = 'white'
        r = app.r*5 - i*app.r
        canvas.create_oval(app.cx - r, app.cy -r, \
                           app.cx + r, app.cy + r, \
                           fill=color)

runApp(width=800, height=600)
