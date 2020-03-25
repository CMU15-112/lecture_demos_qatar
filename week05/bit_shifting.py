import ImageWriter

mypic = ImageWriter.loadPicture("souq_shift.png")

ImageWriter.showPicture(mypic)

width = ImageWriter.getWidth(mypic)
height = ImageWriter.getHeight(mypic)

for i in range(width):
    for j in range(height):
        r,g,b = ImageWriter.getColor(mypic, i, j)
        
        r = (r & 0x07) << 5
        g = (g & 0x07) << 5
        b = (b & 0x07) << 5

        ImageWriter.setColor(mypic,i,j,[r,g,b])

ImageWriter.updatePicture(mypic)