# print coordinates

maxY= 8
maxX= 6

for y in range(maxY+1):
    for x in range(maxX+1):
        print("(",x,",",y, ")", end="")
    print()
            
# print stars

for y in range(7):
    for x in range(5):
        print("*", end=" ")
    print()