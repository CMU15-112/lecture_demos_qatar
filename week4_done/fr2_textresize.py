from cmu_graphics import *

def redrawAll(app):
    shapeWidth = app.width // 2
    shapeHeight = app.height // 2
    topLeftX = app.width // 2 - shapeWidth //2
    topLeftY = app.height //2 - shapeHeight //2
    drawRect(0,0,app.width, app.height, fill="blue")
    drawRect(topLeftX, topLeftY, shapeWidth, shapeHeight, fill="red")
    fontSize = app.height // 10
    drawLabel("Hi", app.width//2,
              app.height//2, fill="green",
              size=fontSize)

runApp(300, 300)