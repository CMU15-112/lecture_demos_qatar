from cmu_graphics import *


def redrawAll(app):
    drawRect(app.width//2, app.height//2, 200, 100, fill= None, border='black', align='center')
    drawOval(app.width//2, app.height//2, 200, 100, fill= None, border='black')
    drawOval(app.width//2, app.height//2, 200, 100, fill= 'red', border='black', rotateAngle= 45)
    #drawOval(app.width//2, app.height//2, 100, 100, fill= 'blue', border='black', rotateAngle= 45)

    
    drawCircle(app.width//2, app.height//2, 50, fill= 'blue')
    
    drawRegularPolygon(app.width//2, app.height//2, 50, 3, fill= 'green')

    drawStar(app.width//2, app.height//2, 50, 5, roundness= 30,  fill= 'yellow')

    drawLine(0, 0, app.width//2, app.height//2)
    drawLine(0, 0, app.width//2, app.height//2, arrowEnd= True, dashes=True)

    
runApp()