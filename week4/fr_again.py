from cmu_graphics import *

def redrawAll(app):
    h = 50 # Height of first rectangle
    
    for i in range(4):
        x0 = 0
        y0 = i*h 
        w = 400 - (i)*100
        drawRect(x0, y0, w, h, fill="blue")
    drawLabel("again", 200, 180, align='bottom-left',size=h, bold=True)


runApp(400, 200)