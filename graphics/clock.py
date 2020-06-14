import basic_graphics
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
    

def drawClock(canvas, cx, cy, r, hour, minute):
    # simply draws the circular shape
    canvas.create_oval(cx-r, cy-r, cx+r, cy+r, fill="pink", outline="red", width=3)
    
    # text
    for i in range(12):
        # position of text, 12 1 2 3 4 ... 11
        angle = 2*math.pi * i / 12
        a = 0.85*r * math.sin(angle)
        b = 0.85*r * math.cos(angle)
        x = cx + a
        y = cy - b
        # x, y position of the text
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

def draw(canvas, width, height):
    # set the time that you want to display
    hour = 5
    minutes = 30
    drawClock(canvas, width//2, height//2, 100, hour, minutes)

basic_graphics.run(width=400, height=300)