import basic_graphics

def draw(canvas, w, h):
    fontSize = max(w,h)//16
    canvas.create_rectangle(0,0,w,h,fill="blue")
    canvas.create_rectangle(w//4,h//4,w-w//4,h-h//4,fill="red")
    canvas.create_text(w//2,h//2,text="Hi",fill="green",font=f"Arial {fontSize}")

    
basic_graphics.run(width=400, height=300)