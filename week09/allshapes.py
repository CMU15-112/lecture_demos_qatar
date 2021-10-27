import basic_graphics

def drawLineDemo(canvas):
    canvas.create_line(5,5,100,200)
    
def drawSimpleShapesDemo(canvas):
    canvas.create_rectangle(10,10,100,200)
    canvas.create_oval(250, 10, 350, 200)
    canvas.create_rectangle(250, 10, 350, 200)
    canvas.create_oval(50, 50, 100, 100)
    
def drawShapesWithParameters(canvas): 
    canvas.create_rectangle(10,10,100,200, fill="blue", outline="orange", width=2)
    canvas.create_oval(75, 75, 125, 125, fill="white", width=0)

def drawShapesWithCoolColors(canvas): 
    canvas.create_rectangle(10,10,100,200, fill="#978ce6")
    canvas.create_oval(75, 75, 125, 125, fill="#8A1538", width=0)

def drawSomeText(canvas, x, y):
    #canvas.create_text(x, y, text="Hi there!", fill="blue")
    #canvas.create_text(x, y, text="More text", anchor="nw", font="Helvetica 26 underline italic")
    #canvas.create_text(x, y, text="Text Again", anchor="se")
    #canvas.create_text(x, y, text=u'\u265F', anchor="nw", font="Helvetica 26")
    #canvas.create_text(x, y, text=u'\u263a', anchor="nw", font="Helvetica 50")


def draw(canvas, width, height):
    #drawLineDemo(canvas)
    #drawSimpleShapesDemo(canvas)
    #drawShapesWithParameters(canvas)
    #drawShapesWithCoolColors(canvas)
    drawSomeText(canvas, width/2, height/2)
    
    
basic_graphics.run(width=400, height=300)