from cmu_graphics import *

def drawBelgianFlag(x, y, w, h):
    # draw a Belgian flag in the area bounded by (x0,y0) in
    # the top-left
    drawRect(x, y, w//3, h, fill= "black")
    drawRect(x+ w//3, y, w//3, h, fill= "yellow")
    drawRect(x+ 2*w//3, y, w//3, h, fill= "red")


    
    
    

def redrawAll(app):
    # Draw a large Belgian flag
    drawBelgianFlag(10, 10, 100, 70)

    # And draw a smaller one below it
    drawBelgianFlag(10, 90, 50, 35)


    w = 30
    h = 25
    margin = 10
    x = 100
    y = 100
    
    for r in range(4):
        for c in range(6):
            drawBelgianFlag(x, y, w, h)
            x+= (margin+w)
        x = 100
        y += (margin+h)
    
        
            
    
runApp()