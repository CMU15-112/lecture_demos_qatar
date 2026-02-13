from cmu_graphics import *




def drawStackCoins(app, coinCells):
    numRows= 6
    numCols= 7
    
    sideL= app.width//numCols    

    for r in range(numRows):
        for c in range(numCols):
            x = c * sideL
            y = r * sideL
           
            drawRect(x, y, sideL, sideL, fill='blue', border='black')
                        
            if f"{r}{c}" in coinCells:
                circleColor = 'green'
            else:
                circleColor = 'white'
                    
            drawCircle(x+sideL/2, y+sideL/2, sideL/4, fill=circleColor)
            
            
def redrawAll(app):
    #drawStackCoins(app, "")
    drawStackCoins(app, "50,40,53,56")
    

runApp()