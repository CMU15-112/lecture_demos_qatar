# I can create dictionaries using the braces
gulfCapitals = {'Qatar':'Doha', 'Kuwait':'Kuwait City',
                'UAE':'Abu Dhabi', 'Saudi Arabia':'Riyad'}

# I can print it
print(gulfCapitals)

# I can get the value of a key
capital = gulfCapitals['Qatar']
# what's the type of the value stored in variable capital

print(gulfCapitals['Qatar'])

# what about this?
#print(gulfCapitals['qatar']) # this will fail with key error

print(gulfCapitals.get('qatar', "I'm sorry , key not available"))
print(gulfCapitals.get("Oman", "I don't know"))

print(capital)