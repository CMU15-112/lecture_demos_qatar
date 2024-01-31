from cmu_graphics import *


#Rect(left, top, width, height, fill='black', border=None, borderWidth=2,
    #opacity=100, rotateAngle=0, dashes=False, align='left-top', visible=True)
def drawingRectangle(app):
    drawRect(0,0, 100, 200)
    drawRect(0,0, app.width/2, app.height/2)


def changeFill(app):       
    drawRect(0,0, app.width/2, app.height/2, fill='peachPuff') # cs Academy 
    
    drawRect(0,0, app.width/2, app.height/2,
             fill=rgb(200, 20, 60)) #how much does each color contribute (0-255)
    drawRect(0,0, app.width/2, app.height/2,
             fill=rgb(0, 20, 60))
         
    drawRect(0,0, app.width/2, app.height/2, 
             fill=gradient('red', 'purple', start='top-left'))
    drawRect(0,0, app.width/2, app.height/2,
             fill=gradient('red', 'purple', start='center'))
    
def changeBorder(app):
    drawRect(0,0, app.width/2, app.height/2, fill=None, border='blue')
    drawRect(0,0, app.width/2, app.height/2, fill=None, 
             border='blue', borderWidth= 10, dashes=True)

def changeAllignment(app):
    drawRect(app.width/2, app.height/2, app.width/2, 
             app.height/2, fill=None, border='red', borderWidth= 10, 
             dashes=True, align='center')
    drawRect(app.width/2, app.height/2, app.width/2, 
             app.height/2, fill=None, border='red', borderWidth= 10,
             dashes=True, align='bottom-left')

def changeOpacity(app):
    drawRect(app.width/2, app.height/2, app.width/2,
             app.height/2, fill='red', opacity=100)
    drawRect(app.width/2-50, app.height/2-50, app.width/4, 
             app.height/4, fill='blue', opacity=30)
    drawRect(app.width/2-50, app.height/2-50, app.width/4, 
             app.height/4, fill='blue', opacity=70)

#Oval(centerX, centerY, width, height, fill='black', border=None,
     #borderWidth=2, opacity=100, rotateAngle=0, dashes=False,
     #align='center', visible=True)
def drawingOval(app):
    drawOval(app.width/2, app.height/2, app.width/4, 
             app.height/2, fill='red', opacity=100)
    drawOval(app.width/2, app.height/2, app.width/4, 
             app.height/2, fill='red', opacity=100, 
             rotateAngle=20, border='black')
    
    #equal width and height >> circle
    drawOval(app.width/2, app.height/2, app.width/2, 
             app.height/2, fill='red', opacity=100)
    


#Circle(centerX, centerY, radius, fill='black', border=None,
       #borderWidth=2, opacity=100, rotateAngle=0, dashes=False,
       #align='center', visible=True)
    
#Star(centerX, centerY, radius, points, fill='black', border=None,
     #borderWidth=2, roundness=None, opacity=100, rotateAngle=0,
     #dashes=False, align='center', visible=True)

#RegularPolygon(centerX, centerY, radius, points, fill='black', border=None,
               #borderWidth=2, opacity=100, rotateAngle=0, dashes=False,
               #align='center', visible=True)
def drawingOtherShapes(app):
    drawCircle(app.width/2, app.height/2, 100, fill='lightGreen')    
    drawRegularPolygon(app.width/2, app.height/2, 50, 5, fill='lightBlue')
    drawStar(app.width/2, app.height/2, 50, 5, fill='blue')
    drawStar(app.width/2, app.height/2, 50, 5, roundness=50 , fill='blue')


def redrawAll(app):
    drawingRectangle(app)
    #changeFill(app)
    #changeBorder(app)
    #changeAllignment(app)
    #changeOpacity(app)
    #drawingOval(app)
    #drawingOtherShapes(app)
    
runApp()
#runApp(200, 600)