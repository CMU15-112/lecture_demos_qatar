from  cmu_graphics import *
import math
import colorsys


# This is the recursive function
# the depth parameter is actually the inverse of the depth
# it decreases as the recursion gets deeper (for convenience)
# the function draws a line starting from x1,y1 with the given angle
# the parameters spread and length do not change across the calls
# spread is the offset that is applied to the angle to draw the left and right branches
# length is equivalent to the length of the top branches and it is multiplied by the depth to
# determine the length of the line at any given depth (the bigger the depth value, the longer the line)
# because we decrease the depth at each call.

def drawTree(x1, y1, angle, spread, length, depth):
    if depth == 0:
        return
    elif depth > 0:
        #       compute this branch's next endpoint
        x2 = x1 + int(math.cos(math.radians(angle)) * depth * length)
        y2 = y1 + int(math.sin(math.radians(angle)) * depth * length)

        linecolor="black"
        drawLine(x1, y1, x2, y2, lineWidth=int(depth * 0.7)+1 , fill= linecolor)

        # and draw 2 trees, starting from the end point, using recursion
        drawTree(x2, y2, angle - spread, spread, length, depth - 1)
        drawTree(x2, y2, angle + spread, spread, length, depth - 1)

#   Start drawing!
def redrawAll(app):
    # adjust these parameters to get a nice tree
    maxd = 10
    length = 10
    spread = 17
    drawTree(app.width // 2, app.height, -90, spread, length,  maxd)

runApp(width=1200, height=800)
