from cmu_graphics import *
import math

def onAppStart(app):
    app.lineX0 = 200
    app.lineY0 = 400
    app.lineLength = 50
    app.lineX1 = 200
    app.lineY1 = app.lineY0 - app.lineLength
    app.lineAngle = 90
    app.blueR = 10
    app.blueVisible = False
    app.dotsR = 20
    app.dots = [ (100, 180, +2), # cx, cy, dx
                 (140, 150, +1),
                 (200, 150, -3),
                 (200, 210, +3),
                 (260, 180, -1), 
                 (300, 160, +2) ]
    app.diamondsAndStars = [ ]
    app.dotsMoving = False

def getRadiusEndpoint(cx, cy, r, theta):
    return (cx + r*math.cos(math.radians(theta)),
            cy - r*math.sin(math.radians(theta)))

def distance(x0, y0, x1, y1):
    return ((x1 - x0)**2 + (y1 - y0)**2)**0.5

def getRadiusAndAngleToEndpoint(cx, cy, targetX, targetY):
    radius = distance(cx, cy, targetX, targetY)
    angle = math.degrees(math.atan2(cy-targetY, targetX-cx)) % 360
    return (radius, angle)

def redrawAll(app):
    drawLabel('Dot Splotter', 200, 30, size=16)
    drawLabel('Turn the Dots into Diamonds and Stars', 200, 50, size=12)
    drawLabel('Move the mouse to aim', 200, 70, size=12)
    drawLabel('Press space to release the dot', 200, 90, size=12)
    drawLabel('Press m to start/stop dot motion', 200, 110, size=12)
    # draw the line
    drawLine(app.lineX0, app.lineY0, app.lineX1, app.lineY1)
    # draw the orange dots
    for cx, cy, dx in app.dots:
        drawCircle(cx, cy, app.dotsR, fill='orange', border='black')
    # draw the diamonds and the stars
    for i in range(len(app.diamondsAndStars)):
        cx, cy = app.diamondsAndStars[i]
        if i % 2 == 0:
            drawRegularPolygon(cx, cy, app.dotsR, 4,
                               fill='lightGreen', border='black')
        else:
            drawStar(cx, cy, app.dotsR, 4, fill='yellow', border='black')
    # draw the blue dot last
    if app.blueVisible:
        drawCircle(app.blueCx, app.blueCy, app.blueR, fill='blue')

def onKeyPress(app, key):
    if key == 'm':
        app.dotsMoving = not app.dotsMoving
    elif key == 'space':
        app.blueVisible = True
        app.blueAngle = app.lineAngle
        length = app.lineLength + app.blueR
        x, y = getRadiusEndpoint(app.lineX0, app.lineY0, length, app.lineAngle)
        app.blueCx, app.blueCy = x, y

def checkForIntersectingDot(app):
    for i in range(len(app.dots)):
        cx, cy, dx = app.dots[i]
        d = distance(app.blueCx, app.blueCy, cx, cy)
        if d <= app.blueR + app.dotsR:
            # they intersected, so:
            # remove the dot
            app.dots.pop(i)
            # add the diamond or star
            app.diamondsAndStars.append((cx, cy))
            # make the blue dot invisible
            app.blueVisible = False
            # and stop checking for other intersections
            return

def onStep(app):
    if app.dotsMoving:
        for i in range(len(app.dots)):
            cx, cy, dx = app.dots[i]
            cx += dx
            if cx + app.dotsR <= 0:
                cx = app.width - app.dotsR
            elif cx - app.dotsR >= app.width:
                cx = -app.dotsR
            app.dots[i] = (cx, cy, dx)
    if app.blueVisible:
        newX, newY = getRadiusEndpoint(app.blueCx, app.blueCy, 5, app.blueAngle)
        app.blueCx, app.blueCy = newX, newY
        checkForIntersectingDot(app)
        if ((app.blueCx + app.blueR <= 0) or
            (app.blueCx - app.blueR >= app.width) or
            (app.blueCy + app.blueR <= 0)):
            app.blueVisible = False

def onMouseMove(app, mouseX, mouseY):
    if mouseY < app.lineY0:
        radius, angle = getRadiusAndAngleToEndpoint(app.lineX0, app.lineY0,
                                                    mouseX, mouseY)
        app.lineAngle = angle
        app.lineX1, app.lineY1 = getRadiusEndpoint(app.lineX0, app.lineY0,
                                                   app.lineLength, angle)

def main():
    runApp()

main()