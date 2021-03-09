myDict = dict()

myDict["Ryan"] = 5
myDict[4.0] = "Bob"
myDict[6] = [1,2,3]

print(myDict)

print("---")

gulfCapitals = {'Qatar':'Doha', 'Kuwait':'Kuwait City', 'Oman':'Muscat',
                'UAE':'Abu Dhabi', 'Saudi Arabia':'Riyad', 'Bahrain':'Manama'}

print(gulfCapitals)

# The next line causes a crash
#print(gulfCapitals['qatar'])

print(gulfCapitals['Qatar'])

# Make sure I don't index something I shouldn't
if "qatar" in gulfCapitals:
    print(gulfCapitals['qatar'])

if "Qatar" in gulfCapitals:
    print(gulfCapitals['Qatar'])
    
print(gulfCapitals.get("oman"))
print(gulfCapitals.get("oman","not found, sorry!"))
print(gulfCapitals.get("Oman"))

# No duplicate keys allowed
print("---")
d = dict()
d[100] = 5
d[200] = 8
d[300] = 7
d[100] = 9
print(d)

print("---")
for key in d:
    print(d[key])
    
print("---")
d = dict()
d[100] = 1
d[200] = 2
d[300] = 3
d[250] = 4

for key in d:
    print(key)