import basic_graphics
import math
import colorsys

def _from_rgb(rgb):
    """translates an rgb tuple of int to a tkinter friendly color code
    """
    return "#%02x%02x%02x" % rgb   
 
# This is the recursive function
# the depth parameter is actually the inverse of the depth
# it decreases as the recursion gets deeper (for convenience)
# the function draws a line starting from x1,y1 with the given angle
# the parameters spread and length do not change across the calls
# spread is the offset that is applied to the angle to draw the left and right branches
# length is equivalent to the length of the top branches and it is multiplied by the depth to
# determine the length of the line at any given depth (the bigger the depth value, the longer the line)
# because we decrease the depth at each call.
def drawTree(canvas, x1, y1, angle, spread, length, depth):
    if depth == 0:
        # we reached the top of the tree, stop the recursion
        return
    elif depth > 0:
        # compute this branch's next endpoint
        x2 = x1 + int(math.cos(math.radians(angle)) * depth * length)
        y2 = y1 + int(math.sin(math.radians(angle)) * depth * length)
 
        # define the color hue based on the depth 
        (r, g, b) = colorsys.hsv_to_rgb(float(depth) / 10, 1.0, 1.0)
        R, G, B = int(255 * r), int(255 * g), int(255 * b)
 
        # convert the r g b tuple to tkinter compatible color string 
        linecolor = _from_rgb((R,G,B))
        
        # draw a single line, this branch
        # the width of the line is also changing according to the depth
        canvas.create_line(x1, y1, x2, y2, width=int(depth * 0.7) , fill= linecolor)
 
        # and draw 2 trees, starting from the end point, using recursion
        
        drawTree(canvas, x2, y2, angle - spread, spread, length, depth - 1)
        drawTree(canvas, x2, y2, angle + spread, spread, length, depth - 1)
 
#   Start drawing!
def draw(canvas, width, height):
    # adjust these parameters to get a nice image
    maxd = 12
    length = 10
    spread = 17
    canvas.create_rectangle(0,0,width, height, fill="black")
    drawTree(canvas,width // 2, height, -90, spread, length,  maxd)
        
basic_graphics.run(width=1200, height=800)