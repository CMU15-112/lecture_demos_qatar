import copy

def ct3(L):
    d = 50
    M = [ L,
          copy.copy(L),
          copy.deepcopy(L) ]
    for N in M:
        N[0][0] += d
        N[1] = [d]
        d = d + 10
    s = str(M)
    s = s.replace("[","").replace("]","")
    return s
print(ct3([[2],[3]]))  # prints 6 numbers


