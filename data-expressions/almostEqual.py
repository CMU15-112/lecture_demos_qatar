#From lecture, do not change this function
def almostEqual(x, y, epsilon=10**-7):
    return (abs(x - y) < epsilon)



def isDistanceEqualTo3(d):
    return almostEqual(d,3)
    #return (d==3)    



d=(0.1+0.1+0.1)*10.0

if isDistanceEqualTo3(d):
    print("yes, distance is 3")
else:
    print("no, distance is not 3 it is ", d)












# x=6
# y=2*3
# 
# if x==y:
#     print("x=",x, " and y=",y," are equal")
# 
# 
# x=0.3
# y=0.1+0.1+0.1
# 
# if x==y:
#     print("x=",x, " and y=",y," are equal")
# 
# 
# if almostEqual(x,y):
#     print("x=",x, " and y=",y," are equal")
# 
# 
# 
# #print( x==y )
# #print(almostEqual(x, y))
# 
# if almostEqual(x,y):   #if x and y are equal
#     print("They are equal")
# 
