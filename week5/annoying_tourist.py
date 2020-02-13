import ImageWriter

files = ["tourist_1.jpg", "tourist_2.jpg", "tourist_3.jpg", "tourist_4.jpg",
         "tourist_5.jpg", "tourist_6.jpg"]

pictures = []
for file in files:
    pic = ImageWriter.loadPicture(file)
    pictures.append(pic)
    
ImageWriter.showPicture(pictures[4])

width = ImageWriter.getWidth(pictures[4])
height = ImageWriter.getHeight(pictures[4])

for i in range(width):
    ImageWriter.updatePicture(pictures[4])
    for j in range(height):
        red = []
        green = []
        blue = []
        for p in pictures:
            colors = ImageWriter.getColor(p,i,j)
            red.append(colors[0])
            green.append(colors[1])
            blue.append(colors[2])
            
        r = sorted(red)[len(red)//2]
        g = sorted(green)[len(green)//2]
        b = sorted(blue)[len(blue)//2]
        
        ImageWriter.setColor(pictures[4],i,j,[r,g,b])

ImageWriter.updatePicture(pictures[4])
            