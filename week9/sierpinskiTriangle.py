from cmu_graphics import *

# Change this value to adjust how deep the recursion goes
LEVEL=5

def drawSierpinskiTriangle(level, x, y, size):
    # (x,y) is the lower-left corner of the triangle
    # size is the length of a side
    # Need a bit of trig to calculate the top point
    if level == 0:
        topY = y - (size**2 - (size/2)**2)**0.5
        drawPolygon(x, y, x+size, y, x+size/2, topY, fill='black')
    else:
        # Bottom-left triangle
        drawSierpinskiTriangle(level-1, x, y, size/2)
        # Bottom-right triangle
        drawSierpinskiTriangle(level-1, x+size/2, y, size/2)
        # Top triangle
        midY = y - ((size/2)**2 - (size/4)**2)**0.5
        drawSierpinskiTriangle(level-1, x+size/4, midY, size/2)

def redrawAll(app):
    width = app.width
    height = app.height
    margin = min(width, height)//10
    x, y = margin, height-margin
    size = min(width, height) - 2*margin
    drawSierpinskiTriangle(LEVEL, x, y, size)
    drawLabel(f'Level {LEVEL} Fractal',
              width/2, margin,
              font = 'Arial',
              size=int(margin/3),
              bold=True,
              align='top')

runApp(width=400, height=400)
