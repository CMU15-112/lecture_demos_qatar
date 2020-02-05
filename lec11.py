def isAnagram(s1,s2):
    for c in s1:
        if c in s2:
            i = s2.index(c)
            s2 = s2[:i]+s2[i+1:]
            print("Printing s after scratching out a char",s2)
        else:
            if c != " ":
                return False
        
    if len(s2.strip()) != 0:
        return False
    return True


def findNumbers(s):
    num = ""
    A = []
    for c in s:
        if c.isdigit():
            num = num + c
        else:
            if num != "":
              A.append(int(num))
              num = ""
    return A
print (findNumbers("I have 2 apples, 12 bananas, and 34 straws"))
#print (isAnagram("twelve plus one","eleven plus two"))
#print (isAnagram("dormitory","dirty room"))
#print (isAnagram("dormitory","dirty rooms"))
