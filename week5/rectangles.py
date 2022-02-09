import basic_graphics


def draw(canvas, width, height):
    canvas.create_oval(100,100,500,500, fill="blue", width=30)
    canvas.create_oval(250,10,350,200, fill="green", width=5, outline="orange")
    
    


basic_graphics.run(width=800, height=800)