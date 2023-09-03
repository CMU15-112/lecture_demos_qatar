def longest42run(n):
	maxRunSoFar = 0
	countRun = 0

	while n > 0:
		if n%100 == 42:
			countRun += 1
			n = n // 100
			maxRunSoFar = max(maxRunSoFar, countRun)
		else:
			countRun=0
			n = n//10
	return maxRunSoFar

print(longest42run(4242142))



