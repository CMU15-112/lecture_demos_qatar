def extractIntegerNumbers(s):
        answer = ""
	cntN = ""
	for i in range(len(s)):
		c =s[i]
		if c.isdigit():
			cntN = cntN + c
		else:
			if c == '-':
				if cntN == "":  # i wasn't reading a num
					cntN += c   # negative sign in front of a num
				else:  # i was reading a num or a dash
					if i+1 < len(s) and s[i+1].isdigit():
						if cntN != "":
							answer = answer + cntN + ','
							cntN = '-'
			else:
				if cntN != "":
					answer = answer + cntN + ','
				cntN = ''
	return answer[:-1]

print(extractIntegerNumbers("3 dogs, 17 cats, and 14 cows!"))









assert(extractIntegerNumbers("3 dogs, 17 cats, and 14 cows!") =="3,17,14")
assert(extractIntegerNumbers("I saw four dogs")=="")
assert(extractIntegerNumbers("cmu15112 is the best!")=="15112")
assert(extractIntegerNumbers("Five -3 equals 2")=="-3,2")
assert(extractIntegerNumbers("be careful with neg. ints 32-42")=="32,-42")
assert(extractIntegerNumbers("cmu15-112isGr8")=="15,-112,8")
