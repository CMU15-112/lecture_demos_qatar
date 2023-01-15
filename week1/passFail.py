# create the function passOrFail(grade) that
# takes a grade as an integer
# returns the string "Pass" if the grade is greater or
# equal to 60, 
# and returns the string "Fail" otherwise

def passOrFail(grade):
    if grade >= 60:
        return "Pass"
    return "Fail"

assert(passOrFail(50) == "Fail")
assert(passOrFail(60) == "Pass")
assert(passOrFail(-60) == "Fail")
print("Yey")
