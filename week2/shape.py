def printMysteryShape(n):
	for i in range(n):
		print(i,end="")
		for j in range(i):
			print(i,'*',end="")
		print("")

printMysteryShape(5)
