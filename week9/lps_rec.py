def lpsRec(string, start, length):
    if length == 1:
        return 1
    if length == 0:
        return 0
    if string[start] == string[start + length -1]:
        return 2 + lpsRec(string, start + 1, length - 2)
    else:
        return max(lpsRec(string, start + 1, length - 1) , lpsRec(string, start , length - 1))



string='rpamasrm'
print(lpsRec(string, 0, len(string)))