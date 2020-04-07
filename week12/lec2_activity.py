import copy

def ct(arg):
    a = arg
    b = copy.copy(a)
    c = copy.deepcopy(a)
    a[0][1] = 7
    b[1][1] = 8
    c[2][1] = 9
    b[2] = [10, 20]
    print(a)
    print(b)
    print(c)

listOfNums = [[1,2],[3,4],[5,6]]
ct(listOfNums)
print(listOfNums)