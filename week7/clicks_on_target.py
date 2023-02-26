from cmu_112_graphics import *

def appStarted(app):
    app.counter = 0

def mousePressed(app, event):
    cx = app.width //2
    cy = app.height //2
    if (cx - event.x) ** 2 + (cy - event.y) **2 <= 20**2:
        app.counter += 1
        
def redrawAll(app, canvas):
    canvas.create_text(app.width/2, 100,
                       text=f'{app.counter} clicks on the target',
                       font='Arial 20 bold',
                       fill='black')
    for i in range(5):
        if i%2 == 0:
            color = 'black'
        else:
            color = 'white'
        r = 100 - i*20
        canvas.create_oval(app.width/2 - r, app.height/2 -r, \
                           app.width/2 + r, app.height/2 + r, \
                           fill=color)

runApp(width=800, height=800)