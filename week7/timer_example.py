from cmu_112_graphics import *
# every mouse pressed, draw a green dot, 20 px radius, at the position of
# the mouse pressed

def appStarted(app):
    app.seconds = 0
    app.timerDelay = 1000

def timerFired(app):
    app.seconds += 1
    

def redrawAll(app, canvas):
    canvas.create_text(app.width/2, app.height/2,
                       text=f'{app.seconds} seconds',
                       font='Arial 30 bold',
                       fill='black')

  
runApp(width=800, height=600)