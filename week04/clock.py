from cmu_graphics import *
import math

def drawClockFace(cx, cy, r):
    drawCircle(cx, cy, r, borderWidth=2, fill=None, border='black')
    

def drawNumbers(cx, cy, r):
    r*=0.9
    
    fs= r*0.2
    
    num= 3
    for angle in range(0, 360, 30):
        
        angleR= math.radians(angle)
        x= cx+ r* math.cos(angleR)
        y= cy- r*math.sin(angleR)
        

        drawLabel(num, x, y, size=fs)
        
        num-=1
        
        if(num==0):
            num=12
            
            
        
def drawHandles(cx, cy, r, hour, minutes):
    
    hour+= (minutes/60)
    
    rh=r*0.5
    
    hrAngle= -30*hour+90
    
    if(hrAngle<0):
        hrAngle+=360
    hrAngleR= math.radians(hrAngle)
    # hrAngleR = math.pi/2 - 2*math.pi*hour/12
    
    x= cx+ rh* math.cos(hrAngleR)
    y= cy- rh*math.sin(hrAngleR)
    
    drawLine(cx, cy, x, y, arrowEnd= True, lineWidth=2)



    rm= r*0.8
    
    mAngle= -6*minutes+90
    if(mAngle< 0):
        mAngle+=360
    
    mAngleR= math.radians(mAngle)
    #    mAngleR = math.pi/2 - 2*math.pi*minutes/60

    mx= cx+ rm * math.cos(mAngleR)
    my= cy - rm* math.sin(mAngleR)

    drawLine(cx, cy, mx, my, arrowEnd= True, lineWidth=2)
    
def onAppStart(app):
    print("App Started")

    app.hour = 2
    app.minute= 30
    print(f'my variable is {app.hour}')
    

def onMousePress(app, x, y):
    print(f'mouse press @ {x},{y}')
    app.hour= (app.hour+1 % 12)
    print(f'my variable is {app.hour}')
    

def redrawAll(app):

    cx= app.width//2
    cy= app.height//2 
    
    r= min(app.width, app.height)//4
    
    drawClockFace(cx, cy, r)
    drawNumbers(cx, cy, r)
    drawHandles(cx, cy, r, app.hour, app.minute)
    
runApp(1000, 1000)