from cmu_112_graphics import *
import random


# appStarted happens when the program starts
# initialize model (variables) that belong to the model
def appStarted(app):
    app.score = 0  # score is in the model
    app.colors = ["red", "blue", "orange", "green"] # colors are now in the model
    app.timerDelay = 4000  # timerDelay to specify how often the timerFired will be executed
    app.winner = False  # this is variable True -> score got equal to 10
    app.blink = False

# for keyboard
def keyPressed(app, event):
    if event.key == "Up":
        print("I pressed Up arrow")
        app.timerDelay += 1000
        if app.timerDelay > 10000:
            app.timerDelay = 10000
        print("timerDelay ", app.timerDelay)
    elif event.key=="Down":
        print("Down")
        app.timerDelay -=1000
        if app.timerDelay < 1000:
            app.timerDelay = 1000
        print("timerDelay ", app.timerDelay)

# for mouse
def mousePressed(app, event):
    print("pos ", event.x, event.y)
    #
    # find col
    if event.x < app.width//4:
        col=0
    elif event.x < app.width//2:
        col=1
    elif event.x < 3*app.width//4:
        col=2
    else:
        col=3

    if app.colors[col] == "red":
        app.score+=1
        # if app.score is equal to 10
        if app.score > 10:
            app.score = 10
        if app.score == 10:
            app.winner = True
            app.timerDelay = 1000
            
# for time-based actions
def timerFired(app):
    # whe should shuffle the colors
    # how to set the timer to fire every 4 seconds
    if not app.winner:
        app.colors = [ app.colors[3]] + app.colors[0:3]
        print("I should shift colors")
    else:
        # if winner true
        # to blick
        # happening one second
        app.blink =  not app.blink
        # if blink true then make it false
        print("blink ", app.blink)


# the main function for the view
# here you draw in the canvas (using the model app.xxxx)
def redrawAll(app, canvas):
    # app.colors are the colors in sequence
    # app.score is the number that represents the current score
    
    canvas.create_rectangle(0, 0, app.width//4 , app.height, fill=app.colors[0])
    canvas.create_rectangle(app.width//4,0, app.width//2, app.height, fill=app.colors[1])
    canvas.create_rectangle(app.width//2, 0, 3*app.width//4 , app.height, fill=app.colors[2])
    canvas.create_rectangle(3*app.width//4, 0, app.width , app.height,fill=app.colors[3])
    if app.winner:
        # draw You win
        if app.blink == True:
            canvas.create_text(app.width//2, app.height//2, text="You win", fill="white", font="Arial 36")
    else:
        canvas.create_text(app.width//2, app.height//2, text=str(app.score), fill="white", font="Arial 36")

runApp(width=400, height=400)