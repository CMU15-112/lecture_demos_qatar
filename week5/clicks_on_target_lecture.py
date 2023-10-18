from cmu_graphics import *
import math
import random


def onAppStart(app):
	app.radius = 100
	app.cx = app.width//2
	app.cy = app.height//2
	app.counter = 0


def onMousePress(app, x, y):
	distanceToTarget = ((app.cx - x) ** 2 + (app.cy - y) **2)**0.5
	if distanceToTarget <= app.radius / 5:
		app.counter += 1

def redrawAll(app):
	drawLabel(f'{app.counter} clicks on the target', 
		app.width//2, 100, size=40, bold=True)
	for i in range(5):
		if i%2 == 0:
			color = 'black'
		else:
			color = 'white'
		r = app.radius - (i * app.radius / 5)
		drawCircle(app.cx, app.cy, r,fill=color)
	#

runApp(800, 600)