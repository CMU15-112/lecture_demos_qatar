import ImageWriter

files = ["tourist_1.jpg", "tourist_2.jpg", "tourist_3.jpg", "tourist_4.jpg",
         "tourist_5.jpg", "tourist_6.jpg"]

m=5
pictures = []
for file in files:
    pic = ImageWriter.loadPicture(file)
    pictures.append(pic)

ImageWriter.showPicture(pictures[m])

width = ImageWriter.getWidth(pictures[m])
height = ImageWriter.getHeight(pictures[m])

for i in range(width):
    ImageWriter.updatePicture(pictures[m])
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
        
        ImageWriter.setColor(pictures[m],i,j,[r,g,b])

ImageWriter.updatePicture(pictures[m])