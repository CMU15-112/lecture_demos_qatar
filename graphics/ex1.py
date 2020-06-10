import basic_graphics

def draw(canvas, width, height):
    # create_line(x1, y1, x2, y2) draws a line from (x1, y1) to (x2, y2)
    #print(type(canvas))
    #canvas.create_line(25, 50, width/2, height/2)  # calling a method
    #canvas.create_rectangle(25,50,width/2,height/2,fill="blue")
    #canvas.create_oval(250, 10, 350, 200)
    #canvas.create_oval(0, 0, width/2, height/2)
    canvas.create_oval(0, 0, 100, 100, dash=(3,5)  )
    # what type of 'canvas'?  object,
    
    #  something.somename(a,b,c,d)  what's 'something?  what's somename?
    # remember: monsterA.attack(....)
    # 


basic_graphics.run(width=400, height=300)