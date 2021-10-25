import basic_graphics
import random

def draw(canvas, width, height):
    d = min(width, height)
    canvas.create_oval(0,0, d, d, width=10 )
    
basic_graphics.run(width=800, height=600)