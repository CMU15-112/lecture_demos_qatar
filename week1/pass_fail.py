# create the function passOrFail(grade) that returns the string "Pass"
# if the grade is greater or equal to 60, 
# and returns the string "Fail" otherwise

def passOrFail(grade):
    print(grade >= 60)
    if grade >= 60:
        return "Pass"
    else:
        return "Fail"
    
print("for 50", passOrFail(50))

resultOf100 = passOrFail(100)
print("100:",resultOf100)

print("60:", passOrFail(60))

