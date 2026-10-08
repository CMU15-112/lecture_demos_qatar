import copy

L = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9, 10]
    ]

print(L)
print(L[1][2])

M = L
N = copy.copy(L)

N[0][1] = 20
N[1] = [10, 15, 18]

print(L)

print(N)

P = copy.deepcopy(L)

N.append([0, 0, 0])