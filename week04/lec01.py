from cmu_graphics import *

def redrawAll(app):
    #drawRect(app.width/4, app.height/4, app.width/2, app.height/2,
    #         fill='chartreuse')
    
    #drawRect(app.width/4, app.height/4, app.width/4, app.height/4,
    #         fill='chartreuse', align="bottom-left")
    
    #drawRect(app.width/4, app.height/4, app.width/2, app.height/2,
    #         fill=rgb(10,200,50))
    
    #drawRect(app.width/4, app.height/4, app.width/2, app.height/2,
    #         fill=gradient('red', 'blue', start='top-right'))
    
    #drawRect(app.width/4, app.height/4, app.width/2, app.height/2,
    #         fill=gradient('blue', 'red', start='top-right'),
    #         border=gradient('darkGreen', 'yellow', start='top-right'),
    #         borderWidth=10)
    
    #drawOval(app.width/4, app.height/4, app.width/2, app.height/2,
    #         fill='chartreuse', align='top-left')
    
    drawCircle(app.width/2, app.height/2, app.height/2)
    
    drawStar(app.width/2, app.height/2, app.height/2, 500, fill='yellow')

runApp(width=800, height=600)