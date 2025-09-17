def splitOddNumbers(s):
    string = ""
    for i in range(len(s)):
        if int(s[i])%2!=0:
            string = string +s[i] + "\n"
        else:
            string = string + s[i]
    return string

number = "1324547"
print(splitOddNumbers(number))