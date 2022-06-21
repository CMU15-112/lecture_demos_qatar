myDict = {}

myDict = dict()


myDict["cmu15112"] = 42
myDict[4.0] = "Bob"
myDict[6] = [1,2,3]


# cmu15112 -> 42
# 4.0 -> "Bob"
# 6 -> [1,2,3]

#letterScores = [1, 3, 3, 2, 1]
#               a  b  c  d  e

letterScores = {'a':1, 'b':3, 'c':3, 'd':2, 'e':1 }

print("Score of a: ", letterScores['a'] )

letterScores['f'] = 4
print(letterScores)

#print("score of g:", letterScores['g'])

scoreOfG = letterScores.get('g', 0)
print("score of g:", scoreOfG)


print(letterScores)

letterScores['a'] = 100
print(letterScores)

for k in letterScores:
    print(k, letterScores[k])

for (k, v) in letterScores.items():
    print(k,v)
    
del letterScores['f']
print(letterScores)




























