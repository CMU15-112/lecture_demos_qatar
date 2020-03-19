import basic_graphics

def drawBelgianFlag(c,x0,y0, x1,y1):
    c.create_rectangle(x0,y0,(x1-x0)/3+x0,y1,fill="black")
    c.create_rectangle((x1-x0)/3 + x0,y0,(x1-x0)*2/3+x0,y1,fill="yellow")
    c.create_rectangle((x1-x0)*2/3+x0,y0,x1,y1,fill="red")

def drawmanyFlags(can,widht,height):
    drawBelgianFlag(can,25,25,175,150)
    drawBelgianFlag(can,75,160,125,200)
    flagW = 100
    flagH = 80
    margin = 5
    startx = 200
    starty = 50
    for r in range(6):
        for c in range(7):
            left = startx + c * (flagW + margin)
            top = starty + r * (flagH + margin)
            right = left + flagW - margin
            bottom = top + flagH - margin
            drawBelgianFlag(can,left, top, right,bottom)
        flagW -= 2
        flagH -= 2

def drawsomeText(c,w,h):
    textsize = w//10
    c.create_text(w/2,h/2,text="Hello",font=f'Arial {textsize} bold')
    
def draw(c, width, height):
    #drawmanyFlags(c,width,height)
    drawsomeText(c, width, height)
basic_graphics.run()






