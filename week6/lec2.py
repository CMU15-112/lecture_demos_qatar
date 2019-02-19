# Updated Animation Starter Code

from tkinter import *

####################################
# customize these functions
####################################

def init(data):
    data.groundLevel = 2/3 * data.height
    data.levelWidth = data.width * 2
    data.bushWidth = 100
    
    data.heroX = 300
    data.dx = 20
    data.heroWidth = data.bushWidth/2
    data.heroColor = "red"
    
    data.heroY = data.groundLevel
    data.dy = 0
    data.ddy = 1
    
    data.scrollX = 150
    
    pass

def mousePressed(event, data):
    # use event.x and event.y
    pass

def keyPressed(event, data):
    # use event.char and event.keysym
    if event.keysym == "Right":
        data.heroX += data.dx
    elif event.keysym == "Left":
        data.heroX -= data.dx
    elif event.keysym == "Up":
        data.dy = 20
    elif event.keysym == "d":
        data.scrollX += data.dx
    elif event.keysym == "a":
        data.scrollX -= data.dx
        
        
    if data.heroX-data.scrollX > data.width-data.heroWidth-50:
        data.scrollX += data.dx
    elif data.heroX-data.scrollX < 50:
        data.scrollX -= data.dx

def timerFired(data):
    data.heroY -= data.dy
    data.dy -= data.ddy
    
    
    if data.heroY >= data.groundLevel and \
        data.heroX > -data.heroWidth and data.heroX < data.levelWidth:
        data.dy = 0
        data.heroY = data.groundLevel

def redrawAll(canvas, data):
    for bushLeft in range(0, data.levelWidth, data.bushWidth):
        bushLeft -= data.scrollX
        canvas.create_oval(bushLeft, data.groundLevel-data.bushWidth/2,
                           bushLeft+data.bushWidth, 
                           data.groundLevel+data.bushWidth/2,
                           fill="darkgreen")
                           
    canvas.create_rectangle(0-data.scrollX, data.groundLevel, 
                            data.levelWidth-data.scrollX, data.height,
                            fill="brown")
    
    heroLoc = data.heroX - data.scrollX
    canvas.create_oval(heroLoc, data.heroY-data.heroWidth,
                       heroLoc+data.heroWidth, data.heroY,
                       fill=data.heroColor)
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

run(800, 400)