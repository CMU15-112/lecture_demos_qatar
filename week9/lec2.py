# Updated Animation Starter Code

from tkinter import *
import random

class Monster(object):
    
    def __init__(self, name, hitPoints, size, color, x, y):
        self.name = name
        self.hp = hitPoints
        self.size = size
        self.color = color
        self.x = x
        self.y = y
        self.dx = 10
        
    def move(self, data):
        self.x +=  self.dx
        if self.x+self.size > data.width or self.x-self.size < 0:
            self.dx *= -1
            
        
    def draw(self, canvas, data):
        canvas.create_oval(self.x-self.size, self.y-self.size,
                           self.x+self.size, self.y+self.size,
                           fill=self.color)

class FlyingMonster(Monster):
    def teleport(self, data):
        self.x = random.randint(0, data.width)
        self.y = random.randint(0, data.height)
                           
class Bat(FlyingMonster):
    
    def __init__(self, name, x, y):
        super().__init__(name, 3, 5, "black", x, y)
        self.dx = 20
    
    def draw(self, canvas, data):
        canvas.create_rectangle(self.x-self.size, self.y-self.size,
                           self.x+self.size, self.y+self.size,
                           fill=self.color)
                           
class FireBat(Bat):
    def __init__(self, name, x, y):
        super().__init__(name, x, y)
        self.color = "orange"
        
class Dragon(FlyingMonster):
    def __init__(self, name, x, y):
        super().__init__(name, 1500, 40, "pink", x, y)
        self.dx = 40
        
    def draw(self, canvas, data):
        pointList = [(self.x, self.y-self.size), 
                     (self.x+self.size, self.y+self.size),
                     (self.x-self.size, self.y+self.size)]
        canvas.create_polygon(pointList, fill=self.color)

####################################
# customize these functions
####################################

def init(data):
    data.monsterList = []
    
    m = Monster("Golem", 20, 13, "grey", data.width//2, data.height//2)
    data.monsterList.append(m)
    
    b = Bat("Larry Blood Sucker", data.width//4, data.height//4)
    data.monsterList.append(b)
    
    f = FireBat("Arambha", data.width//2, 3*data.height//4)
    data.monsterList.append(f) 
    
    dr = Dragon("Puff", data.width//2, data.height-50)
    data.monsterList.append(dr)
    
    if isinstance(f, Dragon):
        print("It is!")
    else:
        print("It is not.")

def mousePressed(event, data):
    # use event.x and event.y
    pass

def keyPressed(event, data):
    # use event.char and event.keysym
    
    # If the user presses f, all flying monsters teleport randomly
    if event.char == "f":
        for m in data.monsterList:
            if isinstance(m, FlyingMonster):
                m.teleport(data)

def timerFired(data):
    for m in data.monsterList:
        m.move(data)

def redrawAll(canvas, data):
    for m in data.monsterList:
        m.draw(canvas, data)
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

run(600, 600)