from cmu_112_graphics import *

def appStarted(app):
    app.seconds = 0
    app.dseconds = 0
    app.counter = 0

def timerFired(app):
    app.counter += 1
    if app.counter%10==0:
        app.seconds += 1
        app.counter = 0
    app.dseconds = (app.dseconds + 1)%10



def redrawAll(app, canvas):
    canvas.create_text(app.width/2, app.height/2,
                       text=f'{app.seconds}:{app.dseconds} seconds',
                       font='Arial 30 bold',
                       fill='black')


runApp(width=800, height=600)
