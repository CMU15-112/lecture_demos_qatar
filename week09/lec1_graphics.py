import basic_graphics

def drawLineDemo(canvas):
    canvas.create_line(15,15,50,100)
    canvas.create_line(100,200,600,800) # This goes off the screen, which is ok
    
def drawSimpleShapesDemo(canvas):
    canvas.create_rectangle(10,10,100,200)
    canvas.create_oval(250,10,350,200)
    
def drawShapesWithParameters(canvas):
    canvas.create_rectangle(10,10,100,200, dash=(3,3))
    canvas.create_oval(250,10,350,200, fill="green", width=5, outline="orange")
    
def drawShapesWithCoolColors(canvas):
    canvas.create_rectangle(10,10,100,200, fill="#049968")
    canvas.create_oval(250,10,350,200, fill="#bdbdd9", width=0)
    
def drawSomeText(canvas, width, height):
    fontSize = height//10
    canvas.create_text(width/2, height/2, text="Hello there",
                       font=f"Arial {fontSize}")
    
def drawTextWithAnchors(canvas, width, height):
    canvas.create_rectangle(50,50, 300,300)
    canvas.create_text(100, 50, text="Hello", font="Arial 50 bold italic underline overstrike",
                       anchor="nw")

def draw(canvas, width, height):
    #drawLineDemo(canvas)
    #drawSimpleShapesDemo(canvas)
    #drawShapesWithParameters(canvas)
    #drawShapesWithCoolColors(canvas)
    #drawSomeText(canvas, width, height)
    drawTextWithAnchors(canvas, width, height)

basic_graphics.run(width=400, height=400)