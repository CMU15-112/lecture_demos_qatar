import ImageWriter

souq = ImageWriter.loadPicture("souq_hd.jpg")
pearl = ImageWriter.loadPicture("pearl_hd.jpg")

ImageWriter.showPicture(souq)

width = ImageWriter.getWidth(souq)
height = ImageWriter.getHeight(souq)

for i in range(width):
    for j in range(height):
        souqColors = ImageWriter.getColor(souq, i, j)
        pearlColors = ImageWriter.getColor(pearl, i, j)
        
        newColor = [0,0,0]
        for k in range(3):
            newColor[k] = int(0.75*souqColors[k]+0.25*pearlColors[k])
        
        ImageWriter.setColor(souq, i, j, newColor)
        
ImageWriter.updatePicture(souq)
