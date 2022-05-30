import basic_graphics
def draw(canvas, width, height):
    canvas.create_rectangle( 0, 0, width, height, fill="blue")
    cx = width//2
    cy = height//2
    wr = width //2
    hr = height//2
    canvas.create_rectangle( cx - wr//2, cy - hr//2,
                             cx + wr//2, cy + hr//2,
                             fill = "red")
    fontsize = min(width, height) // 10
    fs = "bold " + str(fontsize)  # naive way
    fs = "bold %d" % (fontsize)   # python2 way
    fs = f"bold {fontsize}"   # python3 way
    canvas.create_text(width//2, height//2, text="Hi!",
                       fill="green",  font=fs)
    
    

    
basic_graphics.run(width=800, height=800)