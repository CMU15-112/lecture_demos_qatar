# I can create dictionaries using the braces
gulfCapitals = {'Qatar':'Doha', 'Kuwait':'Kuwait City',
                'UAE':'Abu Dhabi', 'Saudi Arabia':'Riyad'}

gulfCapitals["Oman"] = "Muscat"
print(gulfCapitals)

otherCapitals =  {'Oman':'Muscat', 'Bahrain':'Manama'}
gulfCapitals.update(otherCapitals)
print(gulfCapitals)
print("len of dict:", len(gulfCapitals))
