#from tkinter import *
import basic_graphics
def rgbString(red,green,blue):
    return "#%02x%02x%02x"% (red,green,blue)

def drawTwoCircles(canvas, col1, col2):
    canvas.create_oval((40,50),(100,300),fill = col1)
    canvas.create_oval((140,150),(200,200),fill = col2)
    
    
def draw1(canvas, width, height):
    red = rgbString(255,0,0)
    pistachio = rgbString(147,197,114)
    maroon = rgbString(176,48,96)
    #canvas.create_rectangle(10,10,width/2,height/2,fill=pistachio,width=3, outline="green")
    #canvas.create_rectangle(200,100,250,150,fill="blue",width=5)
    #canvas.create_oval(100,50,300,150,fill=maroon)
    #canvas.create_line((100,20),(300,150),fill="red",width=5)
    #canvas.create_text(200,300,text="15-112 Rocks!",fill="purple",font="Times 24 bold italic")
    #canvas.create_polygon(100,30,200,50,300,30,200,10, fill = "orange")    
    drawTwoCircles(canvas,"blue",pistachio)



    #canvas.create_rectangle(250,150,150,40,fill="pink")
##def runWindow():
##    root = Tk()
##    print ("Starting main loop")
##    c = Canvas(root,width=400, height=200,bg = "white")
##    c.pack()
##    draw(c,400,200)
##
##    root.mainloop()
##    print ("Done")


basic_graphics.run()
