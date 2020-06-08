import ImageWriter
import copy

def multiplyListAndInt(l, x):
    for i in range(len(l)):
        l[i] = l[i]*x + 255
        l[i] = min(l[i],255)
        l[i]= max(l[i],0)


myPic = ImageWriter.loadPicture("junk.jpg")

# Make a copy of the original picture so that when I do both
# horizontal and vertical edging, I can use an unmodified source
srcPic = copy.deepcopy(myPic)

ImageWriter.showPicture(srcPic)

width = ImageWriter.getWidth(myPic)
height = ImageWriter.getHeight(myPic)

print(f"w {width} h {height}")
"""
conv = [a, b ,c, \
        d, e , f,\
        g, h, i ]
"""

ul=-1
u=-1
ur=-1
l=-1
s=8
r=-1
dl=-1
d=-1
dr=-1

for i in range(1,width-1):
    for j in range(1,height-1):
        colors_a = ImageWriter.getColor(srcPic, i-1, j-1) # above left
        colors_b = ImageWriter.getColor(srcPic, i, j-1) # above
        colors_c = ImageWriter.getColor(srcPic, i+1, j-1) # above left

        colors_d = ImageWriter.getColor(srcPic, i-1, j) # left
        colors_e = ImageWriter.getColor(srcPic, i, j) # same
        colors_f = ImageWriter.getColor(srcPic, i+1, j) # right


        colors_g = ImageWriter.getColor(srcPic, i-1, j+1) # below left
        colors_h = ImageWriter.getColor(srcPic, i, j+1) # below left
        colors_i = ImageWriter.getColor(srcPic, i+1, j+1) # below left


        new_color = [0,0,0]
        for x in range(3):
            #if colors_h[x] < 100:
            #    print(colors_a[x])
            new_color[x] = (ul*colors_a[x] + u*colors_b[x] + ur*colors_c[x] \
                          + l*colors_d[x] + s*colors_e[x] + r*colors_f[x] \
                          + dl*colors_g[x] + d*colors_h[x] + dr*colors_i[x])

            #print(new_color[x])
            new_color[x] = max(0,new_color[x])
            new_color[x] = min(255,new_color[x])
        #print(new_color)
        ImageWriter.setColor(myPic, i, j, new_color) # same

ImageWriter.updatePicture(myPic)
print("Done")
