import ImageWriter

files = ["tourist_1.jpg", "tourist_2.jpg","tourist_3.jpg", "tourist_4.jpg", "tourist_5.jpg", "tourist_6.jpg"]

pics = []
for file in files:
    pic = ImageWriter.loadPicture(file)
    pics.append(pic)
    
ImageWriter.showPicture(pics[4])

width = ImageWriter.getWidth(pics[4])
height = ImageWriter.getHeight(pics[4])

print("width:",width)
print("height:",height)

for i in range(width):
    ImageWriter.updatePicture(pics[4])
    for j in range(height):
        
        r = []
        g = []
        b = []
        for p in pics:
            colors = ImageWriter.getColor(p, i, j)
            r.append(colors[0])
            g.append(colors[1])
            b.append(colors[2])
        #print(r,g,b)
        
        newColor = [0,0,0]
        newColor[0] = sorted(r)[len(r)//2]
        newColor[1] = sorted(g)[len(g)//2]
        newColor[2] = sorted(b)[len(b)//2]
        
        ImageWriter.setColor(pics[4], i, j, newColor)

ImageWriter.updatePicture(pics[4])