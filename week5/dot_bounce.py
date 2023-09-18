from cmu_graphics import *
import random

# There are some "bugs" in the game
# Can you find them?
# Can you fix them?

# This sets up the model
# It is a helper function to initialize the game
# This way we can also use it when restart
def initGame(app):
    app.dotR = random.randint( 20, 50)  # choose a random radius
    app.dotColor = "red"
    app.dotX = random.randint(app.dotR, app.width - app.dotR)  # choose a random starting loc
    app.dotY = random.randint(app.dotR, app.height - app.dotR)
    app.dx = -1 
    app.dy = 1
    app.countDown = 10  # countdown timer in seconds
    app.gameState = "playing"  # game state variable
    app.blinking = False  # blinking active or not
    app.blinkState = False # when blinking is active, to draw or not to draw

# The entry point of the animation
def onAppStart(app):
    app.stepsPerSecond = 20  # 50 ms = 1000/50 = 20 updates per second
    app.speed = 10           # speed of the dot in pixels per update -> 200 pixels/sec
    app.counter = 0          # used to count how many updates have been made
    initGame(app)            # call the helper function to define game variables
    
    
# The "timer" function
# It runs 20 times per second, as specified by the variable app.stepsPerSecond (see above)
def onStep(app):
    app.counter += 1 
    if app.counter % 20 == 0:  # every 20 counter increments (1 second)
        if app.gameState == "playing":  # only decremement when playing
            app.countDown -= 1
            if app.countDown <= 5:  # blink the last 5 seconds
                app.blinking = True
            if app.countDown == 0:  # game over
                app.gameState = "gameOver"
    
    if app.counter % 10 == 0:  # every 10 counter increments (0.5 second)
        if app.gameState == "playing" and app.blinking:  # in state playing and blinking is active
            app.blinkState = not app.blinkState  # flag to know whether the dot is shown or not
                                                 # during blinking state
    
    # only move when playing
    if app.gameState == "playing":
        # update dot position based on the direction and "speed"
        app.dotX += (app.speed * app.dx)
        app.dotY += (app.speed * app.dy)          
        # bounce: when the dot touches the side edges (left, right)
        # change dx direction
        if app.dotX + app.dotR > app.width or app.dotX - app.dotR < 0:
            app.dx *= -1
        # bounce: when the dot touches the side edges (top, bottom)
        # change dy direction
        if app.dotY + app.dotR > app.height or app.dotY - app.dotR < 0:
            app.dy *= -1

def onMousePress(app, x, y):
    # compute the distance between mouse pointer and the dot 
    distance = ((x - app.dotX)**2 + (y - app.dotY)**2)**0.5
    # if less than radius, then the click was inside the circle
    if distance <= app.dotR:
        app.gameState = "win"  # and we change the game state
        
# This is part of the controller
# It processes the keyboard presses
def onKeyPress(app, key):
    if key == "up":      # increase the speed,, why not?
        app.speed += 1
    if key == "down":
        app.speed -= 1   # decrease the speed, too fast?
        app.speed = max(1, app.speed)  # ensure the speed doesn't become negative
    if key == 'r':
        if app.gameState == "win" or app.gameState == "gameOver":
            initGame(app)  # restart the game
            app.gameState = "playing"
    if key == "p":  # pause/unpause the game
        if app.gameState == "playing":
            app.gameState = "pause"
        else:
            app.gameState = "playing"
    if key == "b":  # toggle blinking 
        if app.gameState == "playing":
            app.blinking = not app.blinking  
        

# This is the view!
# Here we use the gameState variable (from the model, of course)
# to determine which screen we show
def redrawAll(app):
    if app.gameState == "gameOver":  # game over :( 
        # show a big blue screen !
        drawRect(0,0,app.width, app.height, fill="blue")
        drawLabel("Game Over", app.width//2, app.height//2, fill="white", size=60)
    elif app.gameState == "win":  # YOU WON :D
        drawRect(0,0,app.width, app.height, fill="red") 
        drawLabel( "You Won",app.width//2, app.height//2, fill="white", size=60)
    elif app.gameState == "pause":  # game pause, coffee time?
        drawRect(0,0,app.width, app.height, fill="blue")
        drawLabel("Pause", app.width//2, app.height//2, fill="white", size=60)
    else:  # the only option remaining is app.gameState == playing, unless we did something wrong
        drawLabel(f"Time Remaining: {app.countDown}", app.width, app.height, 
            align='right-bottom', size=60)
        # we have two "sub-states": blinking and not blinking
        # defined by an additional boolean variable app.blinking 
        # if app.blinking is True, we use the blinkState to decide whether we show the circle or not
        if app.blinking:  # blinking active, only draw when blinkState is True
            if app.blinkState:
                drawCircle(app.dotX, app.dotY, app.dotR, fill=app.dotColor)
        else:  # blinking inactive, draw always
            drawCircle(app.dotX, app.dotY, app.dotR, fill=app.dotColor)
    

runApp(width=1000, height=1000)