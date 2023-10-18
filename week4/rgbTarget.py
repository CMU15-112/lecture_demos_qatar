from cmu_graphics import *

def redrawAll(app):

    drawRGBTarget(app.width, app.height, 6)

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
    drawLabel("RGB", cx, cy, align = 'left', font="arial", size=fontsize, bold=True, fill='white')

runApp(width=1000, height=1000)