import basic_graphics
import random

def drawTSquare(canvas, x, y, width, color, depth):
    if depth == 0:
        return
    canvas.create_rectangle(x - width //2,
                            y - width //2,
                            x + width//2,
                            y + width//2, fill=None, width=2)
    next_width = width // 2
    drawTSquare(canvas, x - width //2, y - width //2, next_width, color, depth-1)
    drawTSquare(canvas, x - width //2, y + width //2, next_width, color, depth-1)
    drawTSquare(canvas, x + width //2, y - width //2, next_width, color, depth-1)
    drawTSquare(canvas, x + width //2, y + width //2, next_width, color, depth-1)
    
def draw(canvas, width, height):
   drawTSquare(canvas, width//2, height//2, 300, 'blue', 4)

basic_graphics.run(width=1000, height=1000)