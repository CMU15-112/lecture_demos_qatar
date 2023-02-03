def largestNumber(s):
    tokens = s.split()
    maxnum=None
    for token in tokens:
        if token.isdigit():
            number = int(token)
            if maxnum==None:
                maxnum=number
            maxnum=max(maxnum, number)
    return maxnum



