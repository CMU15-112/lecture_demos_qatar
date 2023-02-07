import basic_graphics

def draw(canvas, width, height):
    canvas.create_rectangle(  0,   0, width//2, height, fill="blue")
    canvas.create_rectangle(  width//2,   0, width, height, fill="green")
    canvas.create_oval(  0,   0, width, height, fill="red")
    print("I'm drawing")
    
basic_graphics.run(width=800, height=600)
