def hash_string(s):
    sum = 0
    for c in s:
        sum = sum + (ord(c)-ord('a'))
    return sum

while True:
    word = input("Give me a word: ")
    wordHash = hash_string(word) % 16
    print(f"Hash is {wordHash}")
