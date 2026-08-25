def conditionalExample(x):
    if x != 5:
        print("Yep, this is big")
        print("Another line")
    else:
        print("That is small")
        
    print("Thanks for calling me")
    
conditionalExample(5)

print("---")

def moreConditionalExamples(x, y):
#     # Bad idea, the pyschopath is coming for you
#     if x > 5:
#         if y > 5:
#             print("Both numbers are big")
    if x > 5 and y > 5:
        print("Both numbers are big!")
    elif x > 5 or y > 5:
        print("One number is big")
        
moreConditionalExamples(4, 6)

def scoreToLetterGrade(score):
    if score > 100 or score < 0:
        return "Invalid"
    
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "R"
        
x = scoreToLetterGrade(91)
print(x)

print(scoreToLetterGrade(85))
print(scoreToLetterGrade(49))
print(scoreToLetterGrade(90.1))
print(scoreToLetterGrade(105))


