import ImageWriter

souq = ImageWriter.loadPicture("souq_hd.jpg")
thanos = ImageWriter.loadPicture("thanos_green.jpg")

ImageWriter.showPicture(thanos)

width = ImageWriter.getWidth(souq)
height = ImageWriter.getHeight(souq)

for i in range(width):
    for j in range(height):
        souqColors = ImageWriter.getColor(souq, i, j)
        thanosColors = ImageWriter.getColor(thanos, i, j)
        
        if thanosColors[0] < 50 and thanosColors[2] < 50 \
            and thanosColors[1] > 200:
            newColors = souqColors
        else:
            newColors = thanosColors
            
        ImageWriter.setColor(thanos,i,j,newColors)

ImageWriter.updatePicture(thanos)