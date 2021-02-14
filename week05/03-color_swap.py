import ImageWriter

mypic = ImageWriter.loadPicture("souq_hd.jpg")

ImageWriter.showPicture(mypic)

width = ImageWriter.getWidth(mypic)
height = ImageWriter.getHeight(mypic)

for i in range(width):
    for j in range(height):
        colors = ImageWriter.getColor(mypic, i, j)
        newColor = [colors[2], colors[0], colors[1]]
        ImageWriter.setColor(mypic, i, j, newColor)
        
ImageWriter.updatePicture(mypic)
