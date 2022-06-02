from cmu_112_graphics import *
    
def appStarted(app):
    app.counter = 0
    app.timerDelay = 2000
    
# This is called every time one key is pressed
def keyPressed(app, event):
    if event.key == "Space":
        app.counter += 1

def mousePressed(app, event):
    print(f"clicked at {event.x} {event.y}") 
    print("Mouse pressed")

def redrawAll(app, canvas):
    canvas.create_text(app.width/2, app.height/2,
                       text=f'{app.counter} keypresses',
                       font="Arial 30")


runApp(width=800, height=800)


    

