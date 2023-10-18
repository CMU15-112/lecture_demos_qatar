def isValid2dList(L):
	if not isinstance(L, list):
		return False
	for e in L:
		if not isinstance(e, list):
			return False
	return True

# assume L is a valid 2d list
def isValidSquare2dList(L):
	for row in L:
		if len(L) != len(row):
			return False
	return True

def isMagicSquare(L):
	if not isValid2dList(L):
		return False
	# it is 2d list
	if not isValidSquare2dList(L):
		return False
	for row in L:
		for e in row:
			if not isinstance(e, int):
				return False
	tmpL = []
	for row in L:
		for e in row:
			if e in tmpL:
				return False
			tmpL.append(e)

	sumFirst = sum(L[0])
	for row in L:
		if sum(row) != sumFirst:
			return False
	







	

L1 = [ ['a','b'], ['c', 'd'] ]  # ok
L2 = [['a','b']]  # not square 2d list
L3 = [['a','b'], 'c', 'd'] # not 2d list

#print(isValidSquare2dList(L1))
assert(isValidSquare2dList(L1) == True)
assert(isValidSquare2dList(L2) == False)
assert(isValid2dList(L3) == False)

