def largestNumber(s):
	maxNum = None  # we could also use -1
	for w in s.split():
		if w.isdigit():
			n = int(w)
			if maxNum == None:  #is the first
				maxNum = n
			else:
				maxNum = max(maxNum, n)
	return maxNum

print(largestNumber("I saw 3 dogs, 17 cats, and 14 cows!"))
print(largestNumber("I saw four dogs"))

#assert(largestNumber("I saw 3 dogs, 17 cats, and 14 cows!")==17)
#assert(largestNumber("I saw four dogs")==None)
