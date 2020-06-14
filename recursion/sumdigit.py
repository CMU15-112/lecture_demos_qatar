# a function that sums the digits of an integer, recursively!


def sumList(l):
    print("sumList ", l)
    if l == []:
        return 0
    else:
        return l[0] + sumList(l[1:])
    
  
sumList([5,3,2,6])
