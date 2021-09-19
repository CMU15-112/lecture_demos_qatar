import ImageWriter

mypic = ImageWriter.loadPicture("souq_hd.jpg")

ImageWriter.showPicture(mypic)

width = ImageWriter.getWidth(mypic)
height = ImageWriter.getHeight(mypic)

print("width:",width)
print("height:",height)

for i in range(width):
    for j in range(height):
        colors = ImageWriter.getColor(mypic, i, j)
        avg = sum(colors)//3
        if avg > 75:
            newColor = [0,0,0]
        else:
            newColor = [255,255,255]
        ImageWriter.setColor(mypic,i,j,newColor)
    
ImageWriter.updatePicture(mypic)
        

