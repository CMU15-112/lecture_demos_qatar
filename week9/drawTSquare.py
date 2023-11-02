from cmu_graphics import *

def drawTSquare( x, y, width,  depth):
    if depth == 0:
        return
    drawRect(x - width //2,
             y - width //2,
             width,
             width, borderWidth=3, fill=None, border='black')
    next_width = width // 2
    drawTSquare(x - width //2, y - width //2, next_width, depth-1)
    drawTSquare(x - width //2, y + width //2, next_width,  depth-1)
    drawTSquare(x + width //2, y - width //2, next_width,  depth-1)
    drawTSquare(x + width //2, y + width //2, next_width,  depth-1)

def redrawAll(app):
   drawTSquare(app.width//2, app.height//2, 300, 3)


runApp(width=1000, height=1000)
