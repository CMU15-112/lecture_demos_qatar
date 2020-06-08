import ImageWriter

mypic = ImageWriter.loadPicture("souq_hd.jpg")

ImageWriter.showPicture(mypic)

width = ImageWriter.getWidth(mypic)
height = ImageWriter.getHeight(mypic)

for i in range(width):
    for j in range(height):
        r,g,b = ImageWriter.getColor(mypic, i, j)
        
        if r < 40 and g < 40 and b > 40:
            r,g,b = 255,255,255
        
        ImageWriter.setColor(mypic,i,j,[r,g,b])

ImageWriter.updatePicture(mypic)