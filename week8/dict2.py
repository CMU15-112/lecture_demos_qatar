# I can create dictionaries using the braces
gulfCapitals = {'Qatar':'Doha', 'Kuwait':'Kuwait City',
                'UAE':'Abu Dhabi', 'Saudi Arabia':'Riyad'}


# I can print it
print(gulfCapitals)

print( 'Qatar' in gulfCapitals)
print('Doha' in gulfCapitals)




print(len(gulfCapitals))


d = dict()
a = [1] # lists are mutable, so...
d[a] = 42 # Error: unhashable type: 'list'



