from cmu_graphics import *

def onAppStart(app):
    print("Hello")
    app.myVariable = 1
    print(f'my variable is {app.myVariable}')

def onMousePress(app, x, y):
    print(f'mouse press @ {x},{y}')
    app.myVariable += 1
    print(f'my variable is {app.myVariable}')


def redrawAll(app):
    print("hi! from redrawAll")
    print(f"There have been {app.myVariable} mouse presses")
    drawLine(0,0,app.width, 300)

runApp(1200, 600)
