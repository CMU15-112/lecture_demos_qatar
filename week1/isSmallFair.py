def isSmallFair(n):
	if type(n) != int:
		return False
	n = abs(n)
	if 1000 > n or n > 9999:
		return False
	d1 = n%10
	d2 = (n//10)%10
	d3 = (n//100)%10
	d4 = (n//1000)%10
	#print(f'testing digits {d1} {d2} {d3} {d4}')
	sumMod = d1%2 + d2%2 + d3%2 + d4%2
	return sumMod == 2

#assert(isSmallFair(1000) == False)
#assert(isSmallFair(-1000) == False)
assert(isSmallFair(1234))
assert(isSmallFair(-1234))
assert(isSmallFair(15112) == False)
assert(isSmallFair("1234") == False)
assert(isSmallFair(1234.0) == False)
assert(isSmallFair(-1234))
assert(isSmallFair(1123)==False)
assert(isSmallFair(2234)==False)

