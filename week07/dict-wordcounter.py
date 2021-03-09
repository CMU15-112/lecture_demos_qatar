def textCleaner(s):
    badChars = [",",";",".","\"","\' ","\n\'"," \'","!","(",")","?","--",
                "]","[",":"]
    for badChar in badChars:
        s = s.replace(badChar, " ")
    return s.lower()
