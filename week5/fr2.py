import basic_graphics

def draw(canvas, width, height):
    margin = width//4
    canvas.create_rectangle(0,0,width, height, fill="blue")
    canvas.create_rectangle(margin,margin,
                            width-margin, height-margin,
                            fill="red")
    fontsize = height//4
    canvas.create_text(width//2,height//2,
                       text="Hi",
                       font=f"Arial {fontsize}")                      
    

basic_graphics.run(width=600, height=600)