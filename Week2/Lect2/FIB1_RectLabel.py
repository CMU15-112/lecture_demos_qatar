from cmu_graphics import *
   
    
 
def FIB1(app):
    
    w= 50 # with of first rect
    h = 50 #  height of the first rect
    
    for i in range(4):
        
        x= i*w
        
        y= 0
        
        drawRect(x, y, w, (i+1)*h, fill='blue', border= 'black')
        
        
    drawLabel("zing", 0, 25, align= "top-left", size=100, bold= True)   
    

def redrawAll(app):
    FIB1(app)
    
runApp(400, 200)


#runApp(200, 600)