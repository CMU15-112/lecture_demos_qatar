import ImageWriter
import copy

mypic = ImageWriter.loadPicture("souq_hd.jpg")

# Make a copy of the original picture so that when I do both
# horizontal and vertical edging, I can use an unmodified source
srcPic = copy.deepcopy(mypic)

ImageWriter.showPicture(mypic)

width = ImageWriter.getWidth(mypic)
height = ImageWriter.getHeight(mypic)

threshold = 40

for i in range(width):
    previousAverage = 0
    for j in range(height):
        colors = ImageWriter.getColor(srcPic, i, j)
        theAverage = (colors[0]+colors[1]+colors[2])//3
        
        if abs(theAverage - previousAverage) > threshold:
            colors = [0,255,0]
        
        ImageWriter.setColor(mypic,i,j,colors)
        
        previousAverage = theAverage

for j in range(height):
    previousAverage = 0
    for i in range(width):
        modColors = ImageWriter.getColor(mypic, i, j)
        
        colors = ImageWriter.getColor(srcPic, i, j)
        theAverage = (colors[0]+colors[1]+colors[2])//3
        
        # If the pixel is already green from the previous edging,
        # don't change it.
        if modColors != [0,255,0]:    
            if abs(theAverage - previousAverage) > threshold:
                colors = [0,255,0]
            
            ImageWriter.setColor(mypic,i,j,colors)
        
        previousAverage = theAverage
        
ImageWriter.updatePicture(mypic)