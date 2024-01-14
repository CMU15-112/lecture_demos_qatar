# Variables can be redefined
a = 10
a = "Ryan"

# Valid variable names
ageOfTeacher = 42
age_of_teacher = 42 # This is valid, but don't do it in our class
ageOfTeacher1 = 40
ageOfTeacher2 = 45
#1Teacher = 45

# You can modify existing variables
x = 10
x = x + 1
print(x)
x += 1
print(x)
x *= 5
print(x)

# Programmer error: Didn't save the result of the math
x + 5
print(x)