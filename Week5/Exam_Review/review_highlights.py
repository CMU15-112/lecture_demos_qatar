##############  Week 1

x = 100

### expression (no impact) vs statements (changes the program state)
x+6 # expression 
x = x+1 # statement 
print("n") # statement 

### print vs return
def f():
    return "Hello"
    
f() # return is not print


# ### print/string formatting
print(f"x {x} and {x+1}")
# 
# ### if-else blocks
if x > 90:
    print("x > 90")
    
if x == 10:
    print("1")
elif x == 2:
    print("2")
else:
    print("3")
#     
#     
#     
# 
# 
# ##############  Week 2: Loops
# 
# 
# ## invalid ranges

for i in range(1,1): # OR range(2, 6, -2)   
    print(i)
# 
# ##############  Week 3: Strings
#     
# ##one-line string
# s1= "Hi There" # OR 'Hi There'
# 
# ## multi-line string
s2 = """
Hello
World
"""
s3 = '''
Hello2
World2
'''
# 
# #parse multi-line
for w in s2.split("\n"):
    print(w)

# 
# # construct multi-line string
s = ""
s+= "112\n"
s+= "is Fun !!!"
print(s)
# 
v = "Keep going"
print(v[1::2] + v[-1::-2])
print(v[::-1])