import copy
L = [[1,2,3],[4,5,6]]
M = copy.copy(L)
M[0][1] = 10
print("L",L)
print("M",M)
print("---")
M[1] = "Cat"
print("L",L)
print("M",M)