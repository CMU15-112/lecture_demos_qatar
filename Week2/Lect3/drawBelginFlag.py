from cmu_graphics import *

def drawBelgianFlag(x, y, w, h):
    # draw a Belgian flag in the area bounded by (x0,y0) in
    # the top-left
    drawRect(x,y, w//3, h)
    drawRect(x+ w//3,y, w//3, h, fill='yellow')
    drawRect(x+ w*2//3,y, w//3, h, fill='red')

def redrawAll(app):
    # Draw a large Belgian flag
    drawBelgianFlag(10, 10, 100, 70)

    # And draw a smaller one below it
    drawBelgianFlag(10, 90, 50, 35)

    # Now let's have some fun and draw a whole grid of Belgian flags!
    numRows= 4
    numCols= 6
    x= 100
    y= 100
    margin= 10
    w= 30
    h= 25
    for r in range(numRows):
        for c in range(numCols):
            drawBelgianFlag(x,y, w, h)
            x+= w+margin
        y+= h+margin
        x= 100
            
            
    
runApp()