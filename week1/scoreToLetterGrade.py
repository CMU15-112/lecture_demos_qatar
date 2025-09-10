# 90 or more => A
# between 80 and 89=> B
# between 70 and 79 => C
# between 60 and 69 => D
# 59 or less R

def scoreToLetterGrade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70: #
        return "C"
    elif score >=  60:
        return "D"
    else:
        return "R"


print("95: ", scoreToLetterGrade(95))
print("89: ", scoreToLetterGrade(89))
print("80:", scoreToLetterGrade(80))
#print(scoreToLetterGrade(60))
print("70:",scoreToLetterGrade(70))

    
            