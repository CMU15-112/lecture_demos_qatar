# Given a list of characters, return all possible strings of length 3 that can be formed such that no
# consecutive letters occur in the string
# Example:


def recHelper(letters, words, w):
    if len(w) == 3:
        words.append(w)
        return
    
    for c in letters:
        if len(w) == 0 or c != w[-1]:
            recHelper(letters, words, w+c)
    return
        
def findNonConsecutivePermutations(letters):
    result = []
    recHelper(letters, result, "")
    return result

print(findNonConsecutivePermutations("abc"))