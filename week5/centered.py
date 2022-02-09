import basic_graphics
def draw(canvas, width, height):
    margin = 100
    # Approach #1: Add margin to top/left, subtract margin from bottom/right:
    canvas.create_rectangle(margin, margin, width-margin, height-margin,
                            fill="darkGreen")
    # Approach #2: add/subtract width/height from center (cx, cy)
    (cx, cy) = (width/2, height/2)
    (rectWidth, rectHeight) = (width/4, height/4)
    canvas.create_rectangle(cx - rectWidth/2, cy - rectHeight/2,
                            cx + rectWidth/2, cy + rectHeight/2,
                            fill="orange")
    
    
basic_graphics.run(width=800, height=800)