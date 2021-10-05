import ImageWriter

souq = ImageWriter.loadPicture("souq_hd.jpg")
pearl = ImageWriter.loadPicture("pearl_hd.jpg")

ImageWriter.showPicture(souq)

width = ImageWriter.getWidth(souq)
height = ImageWriter.getHeight(souq)

print("width:",width)
print("height:",height)

for i in range(width):
    for j in range(height):
        souq_colors = ImageWriter.getColor(souq, i, j)
        pearl_colors = ImageWriter.getColor(pearl, i, j)
        
        newColor = [0,0,0]
        for k in range(3):
            newColor[k] = int(0.9*souq_colors[k]+0.1*pearl_colors[k])
        
        ImageWriter.setColor(souq,i,j,newColor)
    
ImageWriter.updatePicture(souq)
