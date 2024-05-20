from cmu_graphics import *

def redrawAll(app):
    # drawing code
    print(f" in redrawAll width {app.width} and {app.height}")
    
    #Basic Rect
    #drawRect(0, 0, app.width//2, app.height//2)
    #drawRect(50, 50, app.width//2, app.height//4)

    ##### parameters
    # fill 
    #drawRect(50, 50, app.width//2, app.height//4, fill='peachPuff')
    #drawRect(50, 50, app.width//2, app.height//4, fill=rgb(20, 200, 150))
    #maroon= rgb(176, 48, 96)
    #drawRect(50, 50, app.width//2, app.height//4, fill=maroon)
    #drawRect(50, 50, app.width//2, app.height//4, fill=gradient('red', 'purple', start='center'))
    #drawRect(50, 50, app.width//2, app.height//4, fill=gradient('red', 'purple', start='top-left'))
    
    # border
    #drawRect(50, 50, app.width//2, app.height//4, fill='peachPuff', border='black')
    #drawRect(50, 50, app.width//2, app.height//4, fill=None, border='black', borderWidth= 5, dashes=True)

    # align
    #drawRect(app.width//2, app.height//2, app.width//2, app.height//4, fill='peachPuff', border='black', align='center')
    #drawRect(app.width//2, app.height//2, app.width//2, app.height//4, fill='peachPuff', border='black', align='bottom-right')

    # rotation
    #drawRect(app.width//2, app.height//2, app.width//2, app.height//4, fill='peachPuff', border='black', rotateAngle=45)
    #drawRect(app.width//2, app.height//2, app.width//2, app.height//4, fill='peachPuff', border='black', rotateAngle=-45, align='center')
    
    #opacity
    drawRect(app.width//2, app.height//2, app.width//2, app.height//4, fill='red', border='black', align='center')
    #drawRect(app.width//2, app.height//2, app.width//2, app.height//4, fill='blue', border='black', rotateAngle=45, opacity= 70)
    drawRect(app.width//2, app.height//2, app.width//2, app.height//4, fill='blue', border='black', rotateAngle=45, opacity= 30)

    # Labels
    #drawLabel("Hello, World!", app.width//2, app.height//2)
    drawLabel("Hello, World!", app.width//2, app.height//2, fill="Orange", size= 50, rotateAngle= 45, font="caveat")

    club= chr(0x2663)
    drawLabel(club, app.width//4, app.height//4, size= 50, rotateAngle= 45, font="caveat")



runApp()
#runApp(200, 600)