import ImageWriter

mypic = ImageWriter.loadPicture("souq_hd.jpg")

ImageWriter.showPicture(mypic)

width = ImageWriter.getWidth(mypic)
height = ImageWriter.getHeight(mypic)

thr = 50

for i in range(width):
    previousAverage = None
    for j in range(height):        
        colors = ImageWriter.getColor(mypic, i, j)
        colorAverage = (colors[0]+colors[1]+colors[2])//3
        
        # Don't check the first pixel in every column
        if previousAverage != None:      
            if abs(colorAverage - previousAverage) > thr:
                colors = [0,255,0]
        
        ImageWriter.setColor(mypic, i, j, colors)        
#         if previousAverage != None and abs(colorAverage - previousAverage) > thr:
#             break
        previousAverage = colorAverage

for j in range(height):
    previousAverage = None
    for i in range(width):        
        colors = ImageWriter.getColor(mypic, i, j)
        colorAverage = (colors[0]+colors[1]+colors[2])//3
        
        # Don't check the first pixel in every column
        if previousAverage != None:      
            if abs(colorAverage - previousAverage) > thr:
                colors = [0,255,0]
        
        ImageWriter.setColor(mypic, i, j, colors)
#         if previousAverage != None and abs(colorAverage - previousAverage) > thr:
#             break        
        previousAverage = colorAverage
        
ImageWriter.updatePicture(mypic)
