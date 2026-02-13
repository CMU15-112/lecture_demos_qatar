# Sample string for demonstration
sampleStr = "Hello, World!"

# 1. capitalize() - Capitalizes the first character of the string
print(sampleStr.capitalize())  # Output: "Hello, world!"

# 2. casefold() - Converts the string into lower case (more aggressive than lower())
print(sampleStr.casefold())  # Output: "hello, world!"

# 3. center() - Centers the string with specified width and fill character
print(sampleStr.center(20, '*'))  # Output: "***Hello, World!***"

# 4. count() - Counts occurrences of a substring
print(sampleStr.count('o'))  # Output: 2

# 5. encode() - Encodes the string using the specified encoding
print(sampleStr.encode('utf-8'))  # Output: b'Hello, World!'

# 6. endswith() - Checks if the string ends with the specified suffix
print(sampleStr.endswith('!'))  # Output: True

# 7. expandtabs() - Expands tabs in the string to multiple spaces
tab_str = "Hello\tWorld"
print(tab_str.expandtabs(4))  # Output: "Hello   World"

# 8. find() - Finds the first occurrence of a substring
print(sampleStr.find('World'))  # Output: 7

# 9. format() - Formats the string using the given values
print("Hello, {}!".format("Alice"))  # Output: "Hello, Alice!"

# 10. format_map() - Formats the string using a mapping
mapping = {'name': 'Bob'}
print("Hello, {name}!".format_map(mapping))  # Output: "Hello, Bob!"

# 11. index() - Finds the first occurrence of a substring (raises ValueError if not found)
print(sampleStr.index('World'))  # Output: 7

# 12. isalnum() - Checks if all characters in the string are alphanumeric
print(sampleStr.isalnum())  # Output: False

# 13. isalpha() - Checks if all characters in the string are alphabetic
print("Hello".isalpha())  # Output: True

# 14. isdecimal() - Checks if all characters in the string are decimal
print("12345".isdecimal())  # Output: True

# 15. isdigit() - Checks if all characters in the string are digits
print("12345".isdigit())  # Output: True

# 16. isidentifier() - Checks if the string is a valid identifier
print("Hello_World".isidentifier())  # Output: True

# 17. islower() - Checks if all characters in the string are lowercase
print("hello".islower())  # Output: True

# 18. isnumeric() - Checks if all characters in the string are numeric
print("12345".isnumeric())  # Output: True

# 19. isprintable() - Checks if all characters in the string are printable
print("Hello\nWorld".isprintable())  # Output: False

# 20. isspace() - Checks if all characters in the string are whitespace
print("   ".isspace())  # Output: True

# 21. istitle() - Checks if the string is titlecased
print("Hello World".istitle())  # Output: True

# 22. isupper() - Checks if all characters in the string are uppercase
print("HELLO".isupper())  # Output: True

# 23. join() - Joins the elements of an iterable with the string as a separator
print(", ".join(['apple', 'banana', 'cherry']))  # Output: "apple, banana, cherry"

# 24. ljust() - Left-justifies the string with specified width and fill character
print(sampleStr.ljust(20, '-'))  # Output: "Hello, World!-------"

# 25. lower() - Converts all characters in the string to lowercase
print(sampleStr.lower())  # Output: "hello, world!"

# 26. lstrip() - Removes leading characters (spaces by default)
print("   Hello".lstrip())  # Output: "Hello"

# 27. maketrans() - Returns a translation table usable for str.translate()
trans_table = str.maketrans("H", "J")
print(sampleStr.translate(trans_table))  # Output: "Jello, World!"

# 28. partition() - Splits the string at the first occurrence of the separator
print(sampleStr.partition(','))  # Output: ('Hello', ',', ' World!')

# 29. replace() - Replaces occurrences of a substring with another substring
print(sampleStr.replace('World', 'Universe'))  # Output: "Hello, Universe!"

# 30. rfind() - Finds the last occurrence of a substring
print(sampleStr.rfind('o'))  # Output: 8

# 31. rindex() - Finds the last occurrence of a substring (raises ValueError if not found)
print(sampleStr.rindex('o'))  # Output: 8

# 32. rjust() - Right-justifies the string with specified width and fill character
print(sampleStr.rjust(20, '-'))  # Output: "-------Hello, World!"

# 33. rpartition() - Splits the string at the last occurrence of the separator
print(sampleStr.rpartition(','))  # Output: ('Hello', ',', ' World!')

# 34. rsplit() - Splits the string at the separator (from the right)
print(sampleStr.rsplit(',', 1))  # Output: ['Hello', ' World!']

# 35. rstrip() - Removes trailing characters (spaces by default)
print("Hello   ".rstrip())  # Output: "Hello"

# 36. split() - Splits the string at the separator (from the left)
print(sampleStr.split(','))  # Output: ['Hello', ' World!']

# 37. splitlines() - Splits the string at line breaks
multiline_str = "Hello\nWorld"
print(multiline_str.splitlines())  # Output: ['Hello', 'World']

# 38. startswith() - Checks if the string starts with the specified prefix
print(sampleStr.startswith('Hello'))  # Output: True

# 39. strip() - Removes leading and trailing characters (spaces by default)
print("   Hello   ".strip())  # Output: "Hello"

# 40. swapcase() - Swaps the case of all characters in the string
print(sampleStr.swapcase())  # Output: "hELLO, wORLD!"

# 41. title() - Converts the first character of each word to uppercase
print(sampleStr.title())  # Output: "Hello, World!"

# 42. translate() - Translates the string using the given translation table
print(sampleStr.translate(trans_table))  # Output: "Jello, World!"

# 43. upper() - Converts all characters in the string to uppercase
print(sampleStr.upper())  # Output: "HELLO, WORLD!"

# 44. zfill() - Pads the string on the left with zeros to fill the specified width
print("42".zfill(5))  # Output: "00042"