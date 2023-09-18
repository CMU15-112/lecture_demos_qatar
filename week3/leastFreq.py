def leastFrequentLetters(s):
	# step 1. convert to lowercase
	s = s.lower()

	# step 2. 
	# Create new string with only alphabetical chars
	news = "" 
	for c in s:  # 2
		if c.isalpha():
			news = news + c

	# step 3. Some edge cases
	if news == "":  #3
		return ""
	if len(news) == 1:
		return news

	# step 4. Find out what's the smallest frequency
	lowF = len(news)
	for c in news:
		freq = news.count(c)
		lowF = min(lowF, freq)
	
	# Create a new string with only the characters with 
	# count equal to the smallest frequency
	lowFLetters = ""
	for c in string.ascii_lowercase:  # 
		if news.count(c) == lowF:
			lowFLetters = lowFLetters + c
	# done
	return lowFLetters



