def nondestructiveRemoveEvens(L):
	newL = []
	for e in L:
		if e%2 != 0:
			newL.append(e)
	return newL

def destructiveRemoveEvens(L):
	for e in L[:]:
		if e%2 == 0:
			L.remove(e)



L = [54, 21, 42, 76, 33]
assert(nondestructiveRemoveEvens(L) == [21, 33])

destructiveRemoveEvens(L)
assert(L == [21, 33])

