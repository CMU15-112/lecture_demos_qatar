import basic_graphics

def draw(canvas, width, height):
    canvas.create_rectangle(10,10,400,200,
                            dash=(1,5),
                            fill="blue",
                            outline="orange",
                            width=5)

basic_graphics.run(width=800, height=400)


