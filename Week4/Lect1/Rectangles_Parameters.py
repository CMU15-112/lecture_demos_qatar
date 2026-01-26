from cmu_graphics import *

def redrawAll(app):
    print(f"Width: {app.width}, Height: {app.height}")

    ### Rect(left, top, width, height)
    
    #drawRect(0, 0, 100, 200)
    drawRect(50, 50, app.width//2, app.height//2)
    
    
    ### Parameters
    #fill
    #drawRect(50, 50, app.width//2, app.height//2, fill= 'peachPuff')
  #  drawRect(50, 50, app.width//2, app.height//2, fill= rgb(20, 200, 150))
    #drawRect(50, 50, app.width//2, app.height//2, fill= gradient('red','purple', start='center'))
    drawRect(50, 50, app.width//2, app.height//2, fill= gradient('red','purple', start='top-left'))

    #border: color, width, dashes
    drawRect(0, 0, app.width//2, app.height//2, fill= None, border = 'blue', borderWidth = 5, dashes= True)

    #align
#    drawRect(app.width//2, app.height//2, 50, 50, align = 'center')
    
    # rotateion : + clockwise, - anti-clockise rotation
#    drawRect(app.width//2, app.height//2, 50, 50, align = 'center', rotateAngle =20)
#    drawRect(app.width//2, app.height//2, 50, 50, align = 'center', rotateAngle = -20)


    # opacity: 0 transparent, 100 fully opaque
#    drawRect(app.width//2, app.height//2, 50, 50, align = 'center', rotateAngle = -20, opacity= 70)
    drawRect(app.width//2, app.height//2, 50, 50, align = 'center', rotateAngle = -20, opacity= 30)
 
 
    ###### Label(value, centerX, centerY)
    
   # drawLabel("Hello, World!!", app.width//2, app.height//2)
    drawLabel("Hello, World!!", app.width//2, app.height//2, size = 50, rotateAngle = 20, font="caveat")

    club = chr(0x2663)
    drawLabel(club, 50, 50, size = 50, rotateAngle = 20, font="caveat")

#runApp(200, 600)
runApp()