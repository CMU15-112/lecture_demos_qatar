def dictMax(d):
    maxValue = None
    maxKeys = set()
    for k in d:
        if maxValue == None:
            maxValue = d[k]
            maxKeys = {k}
        elif d[k] > maxValue:
            maxValue = d[k]
            maxKeys = {k}
        elif d[k] == maxValue:
            maxKeys.add(k)
    return maxKeys



def mostCommonValue(d):
    freq = {}
    for k in d:
        value = d[k]
        #freq[value] = freq.get(value, 0) + 1
        if value in freq:
            freq[value] += 1
        else:
            freq[value] = 1
    return dictMax(freq)
