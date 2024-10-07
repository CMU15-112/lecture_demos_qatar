from cmu_graphics import *
import random

def distance(x0, y0, x1, y1):
    return ((y1 - y0) ** 2 + (x1 - x0) ** 2) ** 0.5

def onAppStart(app):
    # Configuration
    app.speed = 10
    app.blips = 0

    # The player
    # Convention: [x, y, radius]
    app.player = [app.width // 2, app.height // 2, 15]

    # The dots
    # Convention: [x, y, r, color, dx, dy]
    app.dots = []

def onStep(app):
    app.blips += 1

    # What does this do?  How often does it do it?
    if app.blips % (5 * app.stepsPerSecond) == 0:
        r = random.randint(20, 40)
        x = random.randint(r, app.width - r)
        y = random.randint(r, app.height - r)
        dx = random.choice([-1, 0, 1])
        dy = random.choice([-1, 0, 1])
        color = random.choice(["red", "blue", "green"])
        app.dots.append([x, y, r, dx, dy, color])

    # Why is this app.dot[:] instead of app.dot?
    for dot in app.dots[:]:
        # What this block of code do?
        dot[0] += dot[3]
        dot[1] += dot[4]
        if dot[0] + dot[2] > app.width or dot[0] - dot[2] < 0:
            dot[3] *= -1
        if dot[1] + dot[2] > app.height or dot[1] - dot[2] < 0:
            dot[4] *= -1

        # What are we checking here?  What happens if it is true?
        d = distance(dot[0], dot[1], app.player[0], app.player[1])
        if d < dot[2] + app.player[2]:
            app.dots.remove(dot)

# What does this add to the gameplay?
def onMousePress(app, x, y):
    for dot in app.dots[:]:
        (dotX, dotY, r, dx, dy, color) = dot
        d = ((x - dotX) ** 2 + (y - dotY) ** 2) ** 0.5
        if d <= r:
            app.dots.remove(dot)

# What happens when the arrows keys are pressed?  What changes in the game?
def onKeyPress(app, key):
    if key == "left":
        app.player[0] -= app.speed
    elif key == "right":
        app.player[0] += app.speed
    elif key == "up":
        app.player[1] -= app.speed
    elif key == "down":
        app.player[1] += app.speed

# What does this player look like?
# (Make a guess, but don't waste a lot of time here.)
def drawPlayer(app):
    x = app.player[0]
    y = app.player[1]
    r = 15
    drawCircle(x, y, r, fill="yellow", border="black")
    drawCircle(x + r / 3, y - r / 3, 2)
    drawCircle(x - r / 3, y - r / 3, 2)
    drawArc(x, y, r, r, 200, 140, fill="yellow", border="black")

# What gets drawn?
def redrawAll(app):
    for dot in app.dots:
        (dotX, dotY, r, dx, dy, color) = dot
        drawCircle(dotX, dotY, r, fill=color)
    drawPlayer(app)


runApp(width=800, height=800)
