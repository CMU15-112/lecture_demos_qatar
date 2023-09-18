s = "hello             15112"
for c in s[::-1]: # loops in reverse, why?
	print(f"This is character {c}")

for w in s.split():  # splits the string using spaces
	print(f'This is word {w}')


# a multi-line string
s = """

ab\n
"""
print(len(s))
