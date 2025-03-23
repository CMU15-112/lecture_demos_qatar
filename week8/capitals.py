# I can create dictionaries using the braces
gulfCapitals = {'Qatar':'Doha', 'Kuwait':'Kuwait City',
                'UAE':'Abu Dhabi', 'Saudi Arabia':'Riyad'}


# I can print it
print(gulfCapitals)

print(gulfCapitals['Qatar'])

print('Oman' in gulfCapitals)

gulfCapitals["Oman"] = "Muscat"

print(len(gulfCapitals))

for c in gulfCapitals:
    print(f"Country {c} has value {gulfCapitals[c
    
    ]}")

#print(gulfCapitals.get('Oman',None))

