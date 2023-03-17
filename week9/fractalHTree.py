import basic_graphics
import random

def drawHTree(canvas, x, y, width, color, depth):
    if depth == 0:
        return
    canvas.create_line(x - width //2, y, x + width//2, y, fill=color, width=depth)
    w = width // (2**0.5)
    canvas.create_line(x - width //2, y - w//2, x - width//2, y + w//2, fill=color, width=depth)
    canvas.create_line(x + width //2, y - w//2, x + width//2, y + w//2, fill=color, width=depth)
    nextw = w // (2**0.5)
    drawHTree(canvas, x - width //2, y - w //2, nextw, color, depth-1)
    drawHTree(canvas, x - width //2, y + w //2, nextw, color, depth-1)
    drawHTree(canvas, x + width //2, y - w //2, nextw, color, depth-1)
    drawHTree(canvas, x + width //2, y + w //2, nextw, color, depth-1)
def draw(canvas, width, height):
   drawHTree(canvas, width//2, height//2, 500, 'green', 4)

basic_graphics.run(width=1000, height=1000)