from cmu_graphics import *


def redrawAll(app):
    drawRect(app.width//2, app.height//2, 200, 100, fill= None, border='black', align='center')
    
    #Oval(centerX, centerY, width, height)
    drawOval(app.width//2, app.height//2, 200, 100, fill= 'red', border='black', align='center', rotateAngle= 20)

    drawOval(app.width//2, app.height//2, 100, 100, fill= 'orange', border='black', align='center', rotateAngle= 20)


    # Circle(centerX, centerY, radius)
    drawCircle(app.width//2, app.height//2, 50)
    
    #RegularPolygon(centerX, centerY, radius, points)
    drawRegularPolygon(app.width//2, app.height//2, 50, 3, fill = 'blue')
    
    #Star(centerX, centerY, radius, points)
    drawStar(app.width//2, app.height//2, 50, 5, fill = 'yellow', roundness= 30)
    
    #Line(x1, y1, x2, y2)
    
  #  drawLine(0, 0, app.width//2, app.height//2)
    drawLine(0, 0, app.width//2, app.height//2, arrowEnd= True, dashes= True)

    
runApp()