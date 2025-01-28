from cmu_graphics import *

# redrawAll runs after every resize event
# how can you check this?
def redrawAll(app):
    print("hi!")
    drawLine(0,0,app.width, 300)

runApp(1200, 600)    




