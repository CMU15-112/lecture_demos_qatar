from cmu_graphics import *

def onAppStart(app):
    print("Hello")
    app.name = input("Name:")
    
def redrawAll(app):
    drawRect(0,0,app.width, app.height, fill="blue")
    drawRect(app.width//4, app.height//4, app.width//2, app.height//2, fill="red")
    drawLabel(f"Hi {app.name}", app.width//2, app.height//2, fill="green", size=50)
    
runApp(600, 600)