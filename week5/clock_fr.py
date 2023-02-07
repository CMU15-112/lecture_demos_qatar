import basic_graphics
import math


def drawClockFace(canvas, width, height):
    radius = min(width, height)//4
    cx, cy = width//2, height//2
    canvas.create_oval(cx-radius,cy-radius,
                            cx+radius ,
                            cy+radius,
                            fill="yellow")
    
def drawNumbers(canvas, width, height):
    radius = min(width, height)//4
    smallRadius = 0.85*radius
    cx, cy = width//2, height//2
    num = 3
    fontSize = min(width,height)//24
    for angle in range(0, 360, 30):
 
        angle = math.radians(angle)
        hourX = cx + smallRadius * math.cos(angle)
        hourY = cy + smallRadius * math.sin(angle)
        label = str(num)
        canvas.create_text(hourX, hourY,
                           text=label,
                           font="Arial {} bold".format(fontSize))
        num += 1
        if num == 13:
            num =1
        

        
    
   
def draw(canvas, width, height):
    drawClockFace(canvas, width, height)
    drawNumbers(canvas,width, height)
    
    
basic_graphics.run(width=600, height=600)