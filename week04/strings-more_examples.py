# Return a list containing all of the numbers in s
# Example:
# If s is "I have 21 cats, 41 dogs, and 30 birds"
# then this will return [21, 41, 30]
def extractNums(s):
    ret = []
    memory = ""
    
    # Loop through all characters, "remember" digits and dump them to the
    # return list when I see a non-digit.
    for c in s:
        if c.isdigit():
            memory += c
        else:
            if memory != "":
                ret.append(int(memory))
                memory = ""

    # If the number is at the end of the string, it will be in memory but
    # not yet dumped.
    if memory != "":
        ret.append(int(memory))

    return ret

print(extractNums("1234567890 I have21 cats, 41dogs, and30birds 876"))

# Determine if s1 and s2 are anagrams.
# Example:
# areAnagrams("dormitory", "dirtyroom")
def areAnagrams(s1, s2):
    # Case insensitive and ignore spaces
    s1 = s1.lower().replace(" ","")
    s2 = s2.lower().replace(" ","")
    
    for c in s1:
        if s1.count(c) != s2.count(c):
            return False
    
    return len(s1) == len(s2)
    
print(areAnagrams("dormitory", "dirtyroom"))
print(areAnagrams("listen", "silent"))
print(areAnagrams("despair", "praised"))
print(areAnagrams("dormitory", "dirtyrooom"))
print(areAnagrams("dormitory", "dirtyrom"))
print(areAnagrams("dormitory", "Dirtyroom"))
print(areAnagrams("astronomer", "moon starer"))
print(areAnagrams("moon starer", "astronomer"))
print(areAnagrams("room", "rooms"))
print(areAnagrams("astronomer", "moon starer!"))