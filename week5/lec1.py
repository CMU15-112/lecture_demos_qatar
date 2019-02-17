"""
a = [ [2, 3, 4], [5, 6, 7] ]

for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end= " ")
    print()
    
for item in a:
    for otherItem in item:
        print(otherItem, end= " ")
    print()
"""
class Struct(object): pass
myBucket = Struct()

myBucket.a = 5
myBucket.b = 6.5
myBucket.c = [1,2,3,4,5]

print(myBucket.c)