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
        
        if souqColors == None:
            print("souq:",i,j)
        if pearlColors == None:
            print("pearl:",i,j)
        
        newColors = [0,0,0]
        for k in range(3):
            newColors[k] = (souqColors[k]+pearlColors[k])//2
            
        ImageWriter.setColor(souq,i,j,newColors)

ImageWriter.updatePicture(souq)

