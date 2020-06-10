import basic_graphics
def drawBelgianFlag(canvas, x0, y0, x1, y1):
    # draw a Belgian flag in the area bounded by (x0,y0) in
    # the top-left and (x1,y1) in the bottom-right
    width = (x1 - x0)
    canvas.create_rectangle(x0, y0, x0+width/3, y1, fill="black", width=0)
    canvas.create_rectangle(x0+width/3, y0, x0+width*2/3, y1,
                            fill="yellow", width=0)
    canvas.create_rectangle(x0+width*2/3, y0, x1, y1, fill="red", width=0)

def draw(canvas, width, height):
    # Draw a large Belgian flag
    drawBelgianFlag(canvas, 50, 50, 150, 100)

    # And draw a smaller one below it
    drawBelgianFlag(canvas, 75, 160, 125, 200)
    top = 50
    left=200
    flagWidth=25
    flagHeight=25
    margin=5
    row=0
    while row < 4:  # row by row
        left = 200
        col = 0
        print("row ", row)
        while col < 6:  # col by col
            drawBelgianFlag(canvas, left, top, left+flagWidth, top+flagHeight)
            col += 1
            left += flagWidth
            left += margin
            print("%d top -left %d %d"%(col, top, left))
        top += flagHeight
        top += margin
        row+=1    
   

basic_graphics.run(width=600, height=400)