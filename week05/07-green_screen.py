import ImageWriter

# Return True if the color should be replace with white,
# False otherwise
def colorShouldBeReplaced(r,g,b):
    thr = [75, 150, 75]
    expected = [40, 247, 44]
    
    if abs(r-expected[0]) < thr[0] and abs(g-expected[1]) < thr[1] and abs(b-expected[2]) < thr[2]:
        #print("Replace color!")
        return True
    
    return False

souq = ImageWriter.loadPicture("souq_hd.jpg")
thanos = ImageWriter.loadPicture("thanos_green.jpg")

ImageWriter.showPicture(thanos)

width = ImageWriter.getWidth(thanos)
height = ImageWriter.getHeight(thanos)

for i in range(width):
    for j in range(height):
        souqColors = ImageWriter.getColor(souq, i, j)
        thanosColors = ImageWriter.getColor(thanos, i, j)
        
        if colorShouldBeReplaced(thanosColors[0], thanosColors[1], thanosColors[2]):
            newColor = souqColors
        else:
            newColor = thanosColors
        
        ImageWriter.setColor(thanos, i, j, newColor)
        
ImageWriter.updatePicture(thanos)

