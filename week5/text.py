import basic_graphics


def draw(canvas, width, height):
    #canvas.create_rectangle(50,50, 300,300)
    canvas.create_text(100, 100, text="Hello", font="Arial 60 bold", anchor="nw" )
    

basic_graphics.run(width=800, height=800)