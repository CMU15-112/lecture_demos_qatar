import ImageWriter

def averageDiff(prev, cur):
    red = abs(prev[0]-cur[0])
    gr = abs(prev[1]-cur[1])
    bl = abs(prev[2]-cur[2])
    return sum([red,gr,bl])//3

mypic2 = ImageWriter.loadPicture("souq_hd.jpg")
mypic = ImageWriter.loadPicture("souq_hd.jpg")

ImageWriter.showPicture(mypic)

width = ImageWriter.getWidth(mypic)
height = ImageWriter.getHeight(mypic)

print("width:",width)
print("height:",height)

prev = None
for i in range(width):
    prev = None
    for j in range(height):
        colors = ImageWriter.getColor(mypic2, i, j)
        
        if prev is not None:
            diff = averageDiff(prev,colors)
            if diff > 25:
                newColor = [0,255,0]
                ImageWriter.setColor(mypic,i,j,newColor)       
        prev = colors
        
prev = None
for j in range(height):
    prev = None
    for i in range(width):
        colors = ImageWriter.getColor(mypic2, i, j)
        
        if prev is not None:
            diff = averageDiff(prev,colors)
            if diff > 25:
                newColor = [0,255,0]
                ImageWriter.setColor(mypic,i,j,newColor)
                
        prev = colors
    
ImageWriter.updatePicture(mypic)
