# Updated Animation Starter Code

from tkinter import *
import random

####################################
# customize these functions
####################################

def init(data):
    data.timerDelay = 100
    data.timersPerSecond = 1000//data.timerDelay
    
    data.timerCounter = 0
    
    # Set initial location of square
    data.squareX = random.randint(0, data.width)
    data.squareY = random.randint(0, data.height)
    #data.squareX = data.width-5
    #data.squareY = data.height-5
    data.dx = 5
    data.dy = 5
    
    data.circles = []
    data.circleColors = ["red", "blue", "green", "yellow", "black", "orange"]
    
    # Chosen somewhat randomly
    data.squareWidth = 30
    pass

def mousePressed(event, data):
    # use event.x and event.y
    pass

def keyPressed(event, data):
    # use event.char and event.keysym
    pass

def timerFired(data):
    data.timerCounter += 1
    
    data.squareX += data.dx
    data.squareY += data.dy
    
    if (data.squareX+data.squareWidth) > data.width:
        data.squareX = data.width-data.squareWidth
        data.dx *= -1
        
    if (data.squareY+data.squareWidth) > data.height:
        data.squareY = data.height - data.squareWidth
        data.dy *= -1
        
    if data.squareY < 0:
        data.dy *= -1
        
    if data.squareX < 0:
        data.dx *= -1
    
    circleX = random.randint(0, data.width)
    circleY = random.randint(0, data.height)
    circleR = random.randint(3, 8)
    circleColor = random.choice(data.circleColors)
    
    data.circles.append( (circleX, circleY, circleR, 
                          circleColor) )
    
    pass

def drawCircle(canvas, circle):
    cx = circle[0]
    cy = circle[1]
    r = circle[2]
    color = circle[3]
    
    canvas.create_oval(cx-r,cy-r,cx+r,cy+r, fill=color)

def redrawAll(canvas, data):

    canvas.create_rectangle(data.squareX, data.squareY,
                            data.squareX+data.squareWidth,
                            data.squareY+data.squareWidth,
                            fill="white")
    
    for circle in data.circles:
        drawCircle(canvas, circle)

                            
    canvas.create_text(data.width//2, data.height//2, 
                        text="%.2f"%(data.timerCounter/data.timersPerSecond),
                        font = "Arial 100")
    pass

####################################
# use the run function as-is
####################################

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window
    init(data)
    # create the root and the canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(600, 500)