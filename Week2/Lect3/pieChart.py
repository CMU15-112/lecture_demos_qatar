from cmu_graphics import *
import math

def drawChart(app, s, t):
    sA= 0
    c= 0
    for p in s.split(","):
        v, l = p.split()
        v= int(v)
        sweepA= (v/t) * 360
        print(f"{l}, startAngle {sA}, sweepAngle {sweepA} ")
        
        if c%3 == 0:
            color= 'blue'
        elif c%3 ==1:
            color = 'purple'
        else:
            color = 'green'
        
        drawArc(app.width//2, app.height//2, app.width//2, app.height//2, sA, sweepA, fill= color, border='black' )
        
        d= app.width//6
        angle= math.radians(sA+ sweepA/2)
        
        xl= app.width//2 + d * math.cos(angle)
        yl= app.height//2 - d* math.sin(angle)
        perc= rounded((v/t)* 100)
        
        drawLabel(f"{l} {perc}%" , xl, yl, size= 30)
        
        sA+= sweepA
        c+=1

def redrawAll(app):
    drawChart(app, "10 CS,5 IS,20 BA", 35)
    
    
runApp(600, 600)