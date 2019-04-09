# Updated Animation Starter Code

from tkinter import *
import random

class Dot(object):
    
    # Model
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.r = random.randint(20,40)
        self.clicked = 0
        
        self.color = random.choice(["red", "blue", "green", "yellow"])
    
    # View
    def draw(self, canvas, data):
        canvas.create_oval(self.x-self.r, self.y-self.r,
                           self.x+self.r, self.y+self.r,
                           fill=self.color)
        canvas.create_text(self.x, self.y, text=str(self.clicked))
        
    def move(self, data):
        pass
        
    # Collision detection
    def contains(self, x, y):
        d = ((self.x-x)**2 + (self.y-y)**2)**0.5
        return d <= self.r
                           
    
class MovingDot(Dot):
    
    def __init__(self, x, y):
        super().__init__(x,y)
        self.speed = 5
        
    def move(self, data):
        self.x += self.speed
        
        if self.x > data.width:
            self.x = self.r

class FlashingMovingDot(MovingDot):
    
    def draw(self, canvas, data):
        if data.slowTimer%2 == 0:
            super().draw(canvas, data)
        

####################################
# customize these functions
####################################

def init(data):
    # load data.xyz as appropriate
    data.dots = []
    data.timerCounter = 0
    data.slowTimer = 0
    pass

def mousePressed(event, data):
    # use event.x and event.y
    for d in reversed(data.dots):
        # Check if x,y is in d
        if d.contains(event.x, event.y):
            d.clicked += 1
            return
    
    if event.x < data.width and event.y < data.height:
        numDot = len(data.dots)%3
        if numDot == 0:
            d = Dot(event.x,event.y)
        elif numDot == 1:
            d = MovingDot(event.x, event.y)
        else:
            d = FlashingMovingDot(event.x, event.y)
            
        data.dots.append(d)
    pass

def keyPressed(event, data):
    # use event.char and event.keysym
    pass

def timerFired(data):
    data.timerCounter += 1
    
    if data.timerCounter % 5 == 0:
        data.slowTimer += 1
    
    for d in data.dots:
        d.move(data)

def redrawAll(canvas, data):
    for d in data.dots:
        d.draw(canvas, data)
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

run(800, 800)