from cmu_graphics import *
import math

def drawChart(app, s, t):
    
    csList = s.split(",") #category string list
    
    startA = 0
    c = 0
    for cs in csList: # for each category string
        
        #### parse string
        v, n = cs.split() # value and name of category
        print(n, v)
        
        #### drawArc
        v = int(v)
        sweepA = (v/t)*360
        
        if c%3==0:
            color = "blue"
        elif c%3==1:
            color = "green"
        else:
            color = "purple"
            
        #drawArc(centerX, centerY, width, height, startAngle, sweepAngle)
        drawArc(app.width//2, app.height//2, app.width//2, app.height//2, startA,
                sweepA, fill = color, border = "black")
        
        ##### drawLabel
        nr = app.width//6 # radius for label
        na = startA+(sweepA//2) #angle for label
        
        nar = math.radians(na)
        nx = app.width//2 + nr* math.cos(nar) # X coord for label
        ny = app.height//2 - nr*math.sin(nar) # Y coord for label
        
        vp = rounded(v/t*100) # value percentage for category
        drawLabel(f"{n} {vp}%", nx, ny, size = 30)
        
        
        # update start angle for next category ARC
        startA += sweepA
        
        #update color variable for next category
        c+=1



def redrawAll(app):
    drawChart(app, "10 CS,5 IS,20 BA", 35)
    
    
runApp(600, 600)