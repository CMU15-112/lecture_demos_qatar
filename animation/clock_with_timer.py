from cmu_112_graphics import *
import math

# Helper function to compute the angle of the hour hand
def getHourAngle(hour, minute):
    #  Some test cases.
    # You could (and should) test each helper function individually
    #  assert(getHourAngle(3,0)==0)
    #  assert(getHourAngle(12,0)==math.pi/2)
    #  assert(getHourAngle(9,0)==math.pi)
    #  6 o'clock -> -pi/2 or 3pi/2
    angle=math.pi/2 - 2*math.pi*(hour + minute/60)/12
    # now make it positive for convenience
    if angle < 0:
        angle += 2*math.pi
    return angle

def getMinuteAngle(minute):
    # write some test cases
    # You could (and should) test each helper function individually
    # assert(getMinuteAngle(0) == math.pi/2)
    # assert(getMinuteAngle(45) == math.pi)
    angle = math.pi/2 - 2*math.pi*minute/60
    # now make it positive for convenience
    if angle < 0:
        angle += 2*math.pi
    return angle
    
# take a canvas, why?
# cx, cy : center of clock
# r: radius
# hour
# minute
def drawClock(canvas, cx, cy, r, hour, minute):
    canvas.create_oval(cx-r, cy-r, cx+r, cy+r, fill="pink", outline="red", width=3)
    
    for i in range(12):
        angle = 2*math.pi * i / 12
        a = 0.85*r * math.sin(angle)
        b = 0.85*r * math.cos(angle)
        x = cx + a
        y = cy - b
        if i == 0:
            theText = str(12)
        else:
            theText = str(i)
        canvas.create_text(x,y,text=theText, font="Helvetica 16 bold")
    
    hourAngle = getHourAngle(hour, minute)
    hourX = cx + 0.5*r * math.cos(hourAngle)
    hourY = cy - 0.5*r * math.sin(hourAngle)
    canvas.create_line(cx, cy, hourX, hourY, width=5)
    
    minuteAngle = getMinuteAngle(minute)
    minuteX = cx + 0.66*r * math.cos(minuteAngle)
    minuteY = cy - 0.66*r * math.sin(minuteAngle)
    canvas.create_line(cx, cy, minuteX, minuteY, width=3)
        
""" we don't need a draw function for animations,
    instead, use redrawAll

def draw(canvas, width, height):
    # set the time that you want to display
    hour = 12
    minutes = 8
    drawClock(canvas, width//2, height//2, 100, hour, minutes)
"""

# animation-part
# model (app)
# just create all the model (variables, objects)
def appStarted(app):
    # the number of milliseconds between calls to timerFired
    # Let's make out clock very fast, each second will increase time by one minute
    # timer will fire each 1000 milliseconds = 1 second
    app.timerDelay = 100
    
    # initial time
    # we keep the "data" of our animation in the object app
    # just time, app.nameOfVariable and use that variable in your animation
    app.hour = 12
    app.minutes = 0

# This function will automatically be called each app.timerDelay milliseconds
# In this example, once every second
# just update data,

def keyPressed(app, event):
    pass

def timerFired(app):
    # just changing hour and minutes
    print("timer fired")
    app.minutes += 1
    if app.minutes == 60:
        app.minutes = 0
        app.hour +=1
    if app.hour == 13:
        app.hour = 0

# view
# this is the function that draws (and keeps updating) the canvas


#  Our model is
# hour
# minutes
# app.hour  (how we make "hour" to be part of the model)
# app.minutes    .... minutes
def redrawAll(app, canvas):   # this is view
    # we already have our function drawClock
    # get the width and height of canvas
    width = app.width
    height = app.height
    clockWidth = 100
    drawClock(canvas, width//2, height//2, clockWidth, app.hour, app.minutes)  # drawClock is a function, drawing in the canvas 
    #drawClock(canvas, width//2, height//2, clockWidth, app.hour, app.minutes)
    
    

# we won't use basic_graphics
# basic_graphics.run(width=400, height=300)
# we use runApp from the library cmu_112_graphics
runApp(width=800, height=400)
