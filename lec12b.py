fd = open("lec12b.py","r")
data = fd.readlines()
for d in data:
    print (d)


fd = open("something.txt","a")
fd.write("second line\n")
fd.close()
