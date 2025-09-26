from cmu_graphics import *

def redrawAll(app):
    shapeWidth = app.width // 2
    shapeHeight = app.height // 2
    drawRect(0,0,app.width, app.height, fill="blue")
    drawRect(app.width//2, app.height//2, shapeWidth, shapeHeight,
             fill="red", align = 'center')
    drawLabel("Hi", app.width//2, app.height//2, fill="green", size=50)

runApp(300, 300)