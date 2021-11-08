from cmu_112_graphics import *

def appStarted(app):
    app.timerDelay = 25
    
    app.blips = 0
    app.imgs = []
    app.imgs.append(app.loadImage('goomba1.png'))
    app.imgs.append(app.loadImage('goomba2.png'))
    app.curImg = 0
    app.x = 200
    app.y = 317
    app.dx = 2
    
    app.goombaTimer = 0

def timerFired(app):
    app.blips += 1
    
    if app.goombaTimer > 0:
        
        if app.goombaTimer < (5000//app.timerDelay)/2:
            app.dx = -2
        
        app.goombaTimer -= 1
        app.x += app.dx
        if app.blips % 10 == 0:
            app.curImg = (app.curImg + 1) % len(app.imgs)

def keyPressed(app, event):
    if event.key == "Space" and app.goombaTimer == 0:
        app.goombaTimer = (5000 // app.timerDelay)
        app.dx = 2

def redrawAll(app, canvas):
    canvas.create_image(app.x, app.y, image=ImageTk.PhotoImage(app.imgs[app.curImg]))

runApp(width=800, height=400)