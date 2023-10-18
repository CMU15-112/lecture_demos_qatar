def isPossibleDate(s):
	if s.count('-') != 2:
		return False
	if len(s) != 10:
		return False
	if s[2] != '-' or s[5] != '-':
		return False
	for w in s.split('-'):
		if not w.isdigit():
			return False
	return True

def reformatDates(s):
	answer = ""
	for w in s.split():
		if isPossibleDate(w):
			L = w.split('-')
			if isValidDate(int(L[0]), int(L[1]), int(L[2])):
				answer = L[1] + "-" + L[0] + "-" + L[2]
			else:
				answer = answer + w + " "
		answer = answer + w + " "
	return answer




assert(reformatDates("Today is 09-28-2021")=="Today is 28-09-2021")
assert(reformatDates("Now 09-28-2021 14-34-59")=="Now 28-09-2021 14-34-59")
assert(reformatDates("Ups 13-00-2021")=="Ups 13-00-2021")
assert(reformatDates("12-01-2021 OK")=="01-12-2021 OK")
assert(reformatDates("Not a date 04-31-2021")=="Not a date 04-31-2021")
assert(reformatDates("Good luck")=="Good luck")