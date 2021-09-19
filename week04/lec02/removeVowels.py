""" write the function remove vowels that takes a string and returns the string with all vowels removed """
def removeVowels(s):
    vowels="aeiou"
    news = ""
    for c in s:
        if c not in vowels:
            news = news + c
    return news

#another way
def removeVowelsv2(s):
    vowels="aeiou"
    news = ""
    for i in range(len(s)):
        if s[i] not in vowels:
            news = news + s[i]
    return news

        

mystr="this is a text"
print(removeVowels(mystr))
print("original is ", mystr)
