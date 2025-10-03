from cmu_graphics import *
import math


def initGame(app):
    app.theWord = "fun"
    app.attemptsRem = 10
    app.guessSoFar = "*"*len(app.theWord)
    app.state = 'play'
    
def onAppStart(app):
    initGame(app)
    
def onKeyPress(app, key):
    if key == '`':
        initGame(app)
    if app.state == 'play':
        revWord = ""
        for i in range(len(app.theWord)):
            if app.theWord[i] == key:
                revWord += key
            else:
                revWord += app.guessSoFar[i]
        app.guessSoFar = revWord
        app.attemptsRem -= 1
            
        if app.attemptsRem == 0:
            app.state = 'gameOver'
        print(f'{app.attemptsRem} {app.state}')
    else:
        print("LOSER!")
    
def drawGuessImproved(app, w):
    sep = 20
    side = (app.width - 2*sep - sep*(len(w)-1))//len(w)
    cx = sep
    cy = app.height//2
    for i in range(len(w)):
        cx += side//2
        drawRect(cx, cy, side, side,
                 align='center', fill='white',
                 border='black')
        drawLabel(w[i], cx, cy,
              align='center',
              size=app.height//15)
        cx += (sep + side//2)
        
def redrawAll(app):
    if app.state == 'play':
         drawLabel(f'Attempts Remaining {app.attemptsRem}',
                  app.width, 0, align='right-top',
                  size=app.height//20)
         drawGuessImproved(app, app.guessSoFar)
    else:
        drawLabel("YOU LOST :'(", app.width//2, app.height//2,
                  size = app.height//10, align='center')
    
runApp(600, 600)