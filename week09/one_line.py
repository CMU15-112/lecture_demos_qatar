import basic_graphics

def draw(canvas, width, height):
    # create_line(x1, y1, x2, y2) draws a line from (x1, y1) to (x2, y2)
    canvas.create_line(25, 50, width/2, height/2)
    
basic_graphics.run(width=400, height=300)