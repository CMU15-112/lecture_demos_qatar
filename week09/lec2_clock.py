import basic_graphics
import math

def drawClock(canvas, cx, cy, r, hour, minute):
    fontSize = int(r//10)
    minuteWidth = r/72
    hourWidth = r/45
    canvas.create_oval(cx-r,cy-r,cx+r,cy+r,width=3,fill="pink",outline="red")
     
    for i in range(12):
        angle = i * (2*math.pi/12)
        a = (0.90*r) * math.sin(angle)
        b = (0.90*r) * math.cos(angle)
        x = cx + a
        y = cy - b
        if i == 0:
            theText = "12"
        else:
            theText = str(i)
        canvas.create_text(x, y, text=theText, font=f"Arial {fontSize} bold")
         
    hourAngle = (hour+minute/60) * (2*math.pi/12)
    hourX = cx + (0.5*r) * math.sin(hourAngle)
    hourY = cy - (0.5*r) * math.cos(hourAngle)
    canvas.create_line(cx, cy, hourX, hourY, width=hourWidth)
    
    minuteAngle = minute * (2*math.pi/60)
    minuteX = cx + (0.8*r) * math.sin(minuteAngle)
    minuteY = cy - (0.8*r) * math.cos(minuteAngle)
    canvas.create_line(cx, cy, minuteX, minuteY, width=minuteWidth)    

def draw(canvas, width, height):
    r = 0.9 * (min(height,width)/2)
    drawClock(canvas, width/2, height/2, r, 1, 50)

basic_graphics.run(width=800, height=800)