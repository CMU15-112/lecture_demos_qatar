from cmu_graphics import *

def redrawAll(app):  
    rectW = 200
    rectH = 100
    drawRect( app.width//2 - rectW//2,   app.height//2 - rectH//2, rectW, rectH, fill="orange")
    
runApp(800, 600)


