from tkinter import *
import math

def drawClock(canvas, cx, cy, r, hour, minute):
    canvas.create_oval(cx-r,cy-r,cx+r,cy+r,fill="pink")
    
    labels = ["na", "١", "٢", "٣", "٤", "٥", "٦", "٧", "٨", "٩", "١٠", "١١", "١٢"]
    
    numberRadius = 8.5*r/10
    for i in range(1,13):
        angle = (2*math.pi)/12*i
        numX = cx + numberRadius*math.sin(angle)
        numY = cy - numberRadius*math.cos(angle)
        
        faceText = labels[i]
            
        canvas.create_text(numX, numY, text=faceText, font="Helvetica 18 bold")
        
    # Draw hour hand
    # canvas.create_line(sx,sy,ex,ey,width=2)
    hourRad = 1*r/2
    hourAngle = (hour+minute/60)*(2*math.pi)/12
    hourX = cx + hourRad*math.sin(hourAngle)
    hourY = cy - hourRad*math.cos(hourAngle)
    
    canvas.create_line(cx,cy,hourX,hourY,width=3)
    
    # Draw minute hand
    # canvas.create_line(sx,sy,ex,ey,width=2)
    minRad = 3*r/4
    minAngle = (minute)*(2*math.pi)/60
    minX = cx + minRad*math.sin(minAngle)
    minY = cy - minRad*math.cos(minAngle)
    
    canvas.create_line(cx,cy,minX,minY,width=3)
    

def draw(canvas, width, height):
    drawClock(canvas, width//2, height//2, min(width//2,height//2)-10, 2, 28)


def runDrawing(width=300, height=300):
    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window
    canvas = Canvas(root, width=width, height=height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    draw(canvas, width, height)
    root.mainloop()
    print("bye!")

runDrawing(400, 200)