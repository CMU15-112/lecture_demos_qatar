from cmu_graphics import *

def onAppStart(app):
    #pass
    print("Hello")
    app.myVariable = 1
    print(f'my variable is {app.myVariable}')

def onMousePress(app, x, y):
    print(f'mouse press @ {x},{y}')
    app.myVariable += 1
    print(f'my variable is {app.myVariable}')

def onKeyPress(app, key):
    print(f'key press @ {key}')

def redrawAll(app):
    drawRect(0,0,app.width, app.height, fill="blue")
    drawRect(app.width//4, app.height//4, app.width//2, app.height//2, fill="red")
    drawLabel("Hi", app.width//2, app.height//2, fill="green", size=50)

runApp(1200, 600)    