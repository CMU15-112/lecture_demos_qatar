# Return a count of how many times letter c occurs in string s
# Ignores case
def letterCounter(s, c):
    s = s.lower()
    c = c.lower()
    count = 0
    for letter in s:
        if letter == c:
            count += 1
    return count

def letterCounter(s, c):
    count = 0
    for letter in s:
        if letter == c.lower() or letter == c.upper():
            count += 1
    return count

# Return the number of vowels in s
def vowelCounter(s):
    count = 0
    for letter in s:
        if letter in "aeiouAEIOU":
            count += 1
    return count

print(letterCounter("Hi there Bob", "e"))
print(letterCounter("Hi there Bob", "b"))

print(letterCounter("Hi there Bob", "B"))

print(vowelCounter("Hi there Bob"))