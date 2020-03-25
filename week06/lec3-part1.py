myDict = dict()

# myDict[key] = value

myDict["Ryan"] = 5
myDict[4.0] = "Bob"
myDict[6] = [1,2,3]

#print(myDict)

gulfCapitals = {'Doha':'Qatar', 'Kuwait City':'Kuwait', 'Muscat':'Oman',
                'Abu Dhabi':'UAE', 'Riyad':'Saudi Arabia', 'Manama':'Bahrain'}

print(gulfCapitals["Doha"])

# Crash!
#print(gulfCapitals["doha"])

if "doha" in gulfCapitals:
    print(gulfCapitals["doha"])
    
if "Muscat" in gulfCapitals:
    print(gulfCapitals["Muscat"])
    
print("---")
for key in gulfCapitals:
    print(key, gulfCapitals[key])
    
print("---")

# Keys are not inherently ordered
d = dict()
d[100] = 5
d[300] = 7
d[200] = 6

for key in d:
    print(d[key])
    
print("---")
# You can't have duplicate keys in the same dictionary
d = dict()
d[100] = 5
d[200] = 8
d[300] = 7
d[100] = 8

for key in d:
    print(key, d[key])