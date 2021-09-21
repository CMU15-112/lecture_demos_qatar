import ImageWriter

def colorShouldBeReplaced(colors):
    thr = 125
    expected = [0,255,0]
    
    if abs(colors[0]-expected[0]) < thr and abs(colors[1]-expected[1]) < thr and abs(colors[2]-expected[2]) < thr:
        return True
    else:
        return False

souq = ImageWriter.loadPicture("souq_hd.jpg")
thanos = ImageWriter.loadPicture("thanos_green.jpg")

ImageWriter.showPicture(thanos)

width = ImageWriter.getWidth(thanos)
height = ImageWriter.getHeight(thanos)

print("width:",width)
print("height:",height)

for i in range(width):
    for j in range(height):
        souq_colors = ImageWriter.getColor(souq, i, j)
        thanos_colors = ImageWriter.getColor(thanos, i, j)
        
        if colorShouldBeReplaced(thanos_colors):
            newColor = souq_colors
        else:
            newColor = thanos_colors
        
        ImageWriter.setColor(thanos,i,j,newColor)
    
ImageWriter.updatePicture(thanos)

