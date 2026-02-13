from cmu_graphics import *


def draw(app):
    x= 0
    y= 0
    d= 100
    
    count = 0
    for i in range(3):
        drawLabel(str(count), x+d//2, y+d//2, size=40)
        drawRect(x, y, d, d, fill=None, border='black')
        d+=50
        count+=1
        x+=0.5*d
        y+=0.5*d

def redrawAll(app):
    draw(app)
    
runApp()
