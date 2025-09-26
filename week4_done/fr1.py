from cmu_graphics import *

def redrawAll(app):
    drawRect(  0,   0, 150, 300, fill="blue")
    drawRect(150,   0, 150, 300, fill="green")
    drawCircle( 150,  150, 150, fill="red")
    
runApp(300, 300)
