# Sample string for demonstration
sampleStr = "Hello, World!"

# capitalize() - Capitalizes the first character of the string
print(sampleStr.capitalize())  # Output: "Hello, world!"

# swapcase() - Swaps the case of all characters in the string
print(sampleStr.swapcase())  # Output: "hELLO, wORLD!"

# isalnum() - Checks if all characters in the string are alphanumeric
print(sampleStr.isalnum())  # Output: False

# isalpha() - Checks if all characters in the string are alphabetic
print("Hello".isalpha())  # Output: True

# isdecimal() - Checks if all characters in the string are decimal
print("12345".isdecimal())  # Output: True

# isnumeric() - Checks if all characters in the string are numeric
print("12345".isnumeric())  # Output: True

# islower() - Checks if all characters in the string are lowercase
print("hello".islower())  # Output: True

# isspace() - Checks if all characters in the string are whitespace
print("   ".isspace())  # Output: True

# istitle() - Checks if the string is titlecased
print("Hello World".istitle())  # Output: True

# isupper() - Checks if all characters in the string are uppercase
print("HELLO".isupper())  # Output: True

# count() - Counts occurrences of a substring
print(sampleStr.count('o'))  # Output: 2

# find() - Finds the first occurrence of a substring
print(sampleStr.find('World'))  # Output: 7

# index() - Finds the first occurrence of a substring (raises ValueError if not found)
print(sampleStr.index('World'))  # Output: 7






