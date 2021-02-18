import ImageWriter

mypic = ImageWriter.loadPicture("souq_hd.jpg")

width = ImageWriter.getWidth(mypic)
height = ImageWriter.getHeight(mypic)

for i in range(width):
    for j in range(height):
        colors = ImageWriter.getColor(mypic, i, j)
        newColor = [colors[1], colors[2], colors[0]]
        ImageWriter.setColor(mypic, i, j, newColor)
        
ImageWriter.savePicture(mypic, "souq_colorful.jpg")