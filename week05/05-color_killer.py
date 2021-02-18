import ImageWriter

# Return True if the color should be replace with white,
# False otherwise
def colorShouldBeReplaced(r,g,b):
    thr = 40
    expected = [131, 179, 243]
    
    if abs(r-expected[0]) < thr and abs(g-expected[1]) < thr and abs(b-expected[2]) < thr:
        return True
    
    return False

mypic = ImageWriter.loadPicture("souq_hd.jpg")

ImageWriter.showPicture(mypic)

width = ImageWriter.getWidth(mypic)
height = ImageWriter.getHeight(mypic)

for i in range(width):
    for j in range(height):
        colors = ImageWriter.getColor(mypic, i, j)
        if colorShouldBeReplaced(colors[0], colors[1], colors[2]):
            newColor = [255,255,255]
        else:
            newColor = colors      
        ImageWriter.setColor(mypic, i, j, newColor)
        
ImageWriter.updatePicture(mypic)
