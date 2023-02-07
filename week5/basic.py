import basic_graphics

def draw(canvas, width, height):
    canvas.create_line(0, 0, width//2, height//2)

basic_graphics.run(width=800, height=400)

