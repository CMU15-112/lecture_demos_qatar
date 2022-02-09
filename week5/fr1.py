import basic_graphics


def draw(canvas, width, height):
    (cx, cy) = (width/2, height/2)
    fontsize = min(width,height)//16
    (rectWidth, rectHeight) = (width/2, height/2)
    canvas.create_rectangle(0,0,width,height,fill="blue")
    canvas.create_rectangle(cx - rectWidth/2, cy - rectHeight/2,
                            cx + rectWidth/2, cy + rectHeight/2,
                            fill="red")
    canvas.create_text(width//2, height//2, text="Hi!", fill="green", font=f"Arial {fontsize}")
    
basic_graphics.run(width=800, height=600)