import ImageWriter

mypic = ImageWriter.loadPicture("souq_hd.jpg")

ImageWriter.showPicture(mypic)

width = ImageWriter.getWidth(mypic)
height = ImageWriter.getHeight(mypic)

for i in range(width):
    for j in range(height):
        colors = ImageWriter.getColor(mypic, i, j)
        colorAverage = (colors[0]+colors[1]+colors[2])//3
        ImageWriter.setColor(mypic,i,j,[colorAverage, colorAverage, colorAverage])
        
ImageWriter.updatePicture(mypic)