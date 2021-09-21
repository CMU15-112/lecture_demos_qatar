import ImageWriter

def colorShouldBeReplaced(colors):
    thr = 57
    expected = [133,181,245]
    
    if abs(colors[0]-expected[0]) < thr and abs(colors[1]-expected[1]) < thr and abs(colors[2]-expected[2]) < thr:
        return True
    else:
        return False

mypic = ImageWriter.loadPicture("souq_hd.jpg")

ImageWriter.showPicture(mypic)

width = ImageWriter.getWidth(mypic)
height = ImageWriter.getHeight(mypic)

print("width:",width)
print("height:",height)

for i in range(width):
    for j in range(height):
        colors = ImageWriter.getColor(mypic, i, j)
        
        if colorShouldBeReplaced(colors):
            newColor = [0,255,0]
        else:
            newColor = colors
            
        ImageWriter.setColor(mypic,i,j,newColor)
    
ImageWriter.updatePicture(mypic)
