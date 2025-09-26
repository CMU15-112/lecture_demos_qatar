from cmu_graphics import *
import math

def redrawAll(app):
    # Assume the canvas is square: app.width == app.height
    canvasSize = app.width  # Since it's always square

    # Base (square) is 1/3 of canvas width
    baseSize = canvasSize // 3
    triangleHeight = int(baseSize * math.sqrt(3) / 2)
    houseHeight = triangleHeight + baseSize  # of the house
    houseWidth = baseSize
    
    # House is centered
    centerX = canvasSize // 2
    centerY = canvasSize // 2
    topY = centerY - houseHeight // 2
    topX = centerX - houseWidth // 2
    
    # Square base center coordinates
    baseCenterX = centerX
    baseCenterY = topY + triangleHeight + baseSize // 2
    
    # Roof center coordinates
    roofCenterX = centerX
    roofCenterY = topY + triangleHeight // 2
    
    # Call the helper functions
    drawBase(baseCenterX, baseCenterY, baseSize)
    drawRoof(roofCenterX, roofCenterY, baseSize)
    
    # optional, see the center of the house
    #drawCircle(centerX, centerY, 3)

# assume (x,y) is the center of the base
def drawBase(x, y, baseSize):
    # Draw the square body of the house
    drawRect(x, y, baseSize, baseSize, fill='lightblue',
             align='center')
    # Draw label "Home" centered in the base
    fontSize = int(baseSize / 5)
    drawLabel('Home', x, y, size=fontSize, bold=True)

def drawRoof(x, y, baseSize):
    # Draw an equilateral triangle as the roof
    # The triangle's base is the same as the width of the house
    # Place the roof right above the body
    
    # Height of an equilateral triangle
    height = baseSize * (3 ** 0.5) / 2

    # Vertices of the triangle, centered at (x, y)
    tipX = x
    tipY = y - height // 2

    leftX = x - baseSize // 2
    leftY = y + height // 2

    rightX = x + baseSize // 2
    rightY = y + height // 2

    drawPolygon(tipX, tipY, leftX, leftY, rightX, rightY, fill='brown')


runApp(600, 600)