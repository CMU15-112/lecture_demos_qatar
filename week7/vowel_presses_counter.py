from cmu_112_graphics import *

# This is called once, when the program starts
def appStarted(app):
    app.counter = 0

# This is called every time one key is pressed
def keyPressed(app, event):
    if event.key in 'aeiou':
        app.counter += 1

# This is called many times per second, each time the canvas will be cleared 
# Remember window resize?
def redrawAll(app, canvas):
    canvas.create_text(app.width/2, app.height/2,
                       text=f'{app.counter} vowel presses', font='Arial 30 bold')

runApp(width=800, height=600)