from cmu_graphics import *


def drawBlueRectangles():
        
    h = 50 # Height of first rectangle
    
    for i in range(4):
        x0 = 0
        y0 = i*h 
        w = 400 - (i)*100
        drawRect(x0, y0, w, h, fill="blue")
    #drawLabel("again", 200, 180, 
        #align='bottom-left',size=h, bold=True)

def drawRGBTarget(w, h, n):
    r = w//2
    dr = r//n
    cx = w//2
    cy = h//2
    fontsize = dr
    for i in range(n):
        if i%3 == 0:
            color = rgb(255,0, 0)
        elif i%3 == 1:
            color = rgb(0,255, 0)
        else:
            color = rgb(0,0,255)
        drawCircle(cx,cy,r, fill= color)
        r -= dr
    drawLabel("RGB", cx, cy, align = 'left', font="arial",
              size=fontsize, bold=True, fill='white') 
    
def redrawAll(app):
    drawBlueRectangles()
    #drawRGBTarget(app.width, app.height, 6)


runApp(400, 200)
#runApp(width=1000, height=1000)