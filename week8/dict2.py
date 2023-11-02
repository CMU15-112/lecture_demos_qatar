# I can create dictionaries using the braces
gulfCapitals = {'Qatar':'Doha', 'Kuwait':'Kuwait City',
                'UAE':'Abu Dhabi', 'Saudi Arabia':'Riyad'}

print(gulfCapitals)

gulfCapitals['Bahrain'] = "Manama"

print(gulfCapitals)

print("The capital of Qatar is", gulfCapitals["Qatar"])

print("The capital of Oman is", gulfCapitals.get("Oman") )
print("I know ", len(gulfCapitals), "capital cities")

#print("The capital of Oman is", gulfCapitals.get("Oman", "I don't know") )
