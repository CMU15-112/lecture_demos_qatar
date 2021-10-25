import basic_graphics
import random

def draw(canvas, width, height):
    # create_line(x1, y1, x2, y2) draws a line from (x1, y1) to (x2, y2)
    x1 = random.randint(0, width)
    x2 = random.randint(0, width)
    y1 = random.randint(0, height)
    y2 = random.randint(0, height)
    canvas.create_line(x1, y1, x2, y2)
    
basic_graphics.run(width=400, height=300)