import basic_graphics

def draw(canvas, width, height):
    # draw a line (0,0) - (100,100)
    canvas.create_line(0, 0, width, height, width=10, dash=(10,2))
    #print("Hello ", width, height)
    

basic_graphics.run(width=600, height=300)