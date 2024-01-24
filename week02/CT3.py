def ct3(x,y):
    for z in range(x, y):
        if z< y/2:
            if z%4 ==0: print (f'b:{z}')
            elif z%2 ==0: print(f'e:{z}')
        elif(x+y+z == 25):
            print(f'c:{z}')
    for z in range(y, x):
        print(f'a:{z}')
    w=0
    for z in range(x, 10*x, x):
        if z<5*x: continue
        elif z>= 7*x: return f'd:{z}+{w}'
        w+=z
    return True
    

print(ct3(4, 14))

