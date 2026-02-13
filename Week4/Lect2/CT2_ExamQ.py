from cmu_graphics import *

def redrawAll(app):
    step = app.width//4
    for i in range(2):
        for j in range(2):
            color = "white" if (i + j) % 2 == 1 else "black"
            drawCircle(step + 2 * step * i, step + 2 * step * j, step / 2,
                       border="black", fill=color)
    drawRect(step, step, 2 * step, 2 * step, border="black", fill="white")
    drawLine(0, app.height, app.width, 0)
    drawLine(step, step, 2 * step, 2 * step)
    

runApp()
