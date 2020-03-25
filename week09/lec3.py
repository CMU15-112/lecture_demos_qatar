import basic_graphics
import math

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
    
    hourAngle = 2*math.pi * (hour + minute/60) / 12
    hourX = cx + 0.5*r * math.sin(hourAngle)
    hourY = cy - 0.5*r * math.cos(hourAngle)
    canvas.create_line(cx, cy, hourX, hourY, width=5)
    
    minuteAngle = 2 * math.pi * minute / 60
    minuteX = cx + 0.66*r * math.sin(minuteAngle)
    minuteY = cy - 0.66*r * math.cos(minuteAngle)
    canvas.create_line(cx, cy, minuteX, minuteY, width=3)
        

def draw(canvas, width, height):
    drawClock(canvas, width//2, height//2, 100, 10, 17)

basic_graphics.run(width=400, height=300)