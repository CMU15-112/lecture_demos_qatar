from cmu_graphics import *

def redrawAll(app):
	drawRect(0, 0, app.width//2, app.height, fill="blue")
	drawRect(app.width//2, 0, app.width//2, app.height, fill="green")
	rad = min(app.height//2,app.width//2 )
	drawCircle(app.width//2, app.height//2, rad, fill="red")

runApp(300, 300)