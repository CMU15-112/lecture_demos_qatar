import copy

bigList = [ [1, 2, 3], [4, 5] ]

A = bigList
B = copy.copy(bigList)
C = copy.deepcopy(bigList)

B[0][1] = 10

#B[1] = [8, 9, 10]

#bigList[1] = [20, 30]

bigList[1] = bigList[1] + [67]
bigList[1][0] = 2

C[1] = copy.copy(bigList[1])

print("bigList:", bigList)
print("A:", A)
print("B:", B)
print("C:", C)