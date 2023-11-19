from cmu_graphics import *
# Import this function to preload images
from cmu_graphics.shape_logic import loadImageFromStringReference

import random
import time

class Sprite:
    def __init__(self, images, x, y, cached = False):
        self.images = []
        if cached:   # preload images
            for imgPath in images:
                img = loadImageFromStringReference(imgPath)
                self.images.append(img)
        else:
            self.images = images
        self.curImg = 0
        self.x = x
        self.y = y
        self.dx = 2
    def nextImage(self):
        self.curImg = (self.curImg + 1) % len(self.images)
    def currentImage(self):
        return self.images[self.curImg]
    def move(self):
        self.x += self.dx

def onAppStart(app):
    USE_CACHED = True  # if true, uses preload images (see above)
    app.N = 40
    app.stepsPerSecond = 30
    app.sprites = []
    for i in range(app.N//2):
        x = random.randint(20, app.width - 200)
        y = random.randint(50, app.height - 50)
        sprite = Sprite(['goomba1.png','goomba2.png'], x, y, cached = USE_CACHED)
        app.sprites.append(sprite)

    for i in range(app.N//2):
        x = random.randint(20, app.width - 200)
        y = random.randint(50, app.height - 50)
        sprite = Sprite(['ghost1.png','ghost2.png'], x, y, cached = USE_CACHED)
        app.sprites.append(sprite)

    app.counter = 0
    app.curImg = 0

    app.x = 200
    app.y = 100
    app.dx = 2
    app.blips = 0

    app.spriteTimer = 5 * app.stepsPerSecond
    app.dx = 2
    app.timer = 0
    app.startTime = time.time()


def onMousePress(app, mouseX, mouseY):
    pass

def onStep(app):
    app.blips += 1
    app.timer = app.blips / app.stepsPerSecond

    if app.spriteTimer > 0:

        if app.spriteTimer < (5*app.stepsPerSecond)/2:
            for sprite in app.sprites:
                sprite.dx = -2

        app.spriteTimer -= 1
        for sprite in app.sprites:
            sprite.move()

        if app.blips % 5 == 0:
            for sprite in app.sprites:
                sprite.nextImage()
    else:
        app.spriteTimer = 5 * app.stepsPerSecond
        for sprite in app.sprites:
            sprite.dx = 2



def redrawAll(app):
    for sprite in app.sprites:
        drawImage(sprite.currentImage(), sprite.x, sprite.y)
    drawLabel(f'App Time: {app.timer:.2f}', app.width//4, 60, size = 50)

    realTime = time.time() - app.startTime
    drawLabel(f'Real Time: {realTime:.2f}', 2*app.width//4,  60, size = 50)

    diffTime = app.timer - realTime
    drawLabel(f'Diff: {diffTime:.2f}', 3*app.width//4,  60, size = 50)

runApp(width= 1200, height = 800)
