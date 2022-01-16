# another example of conditionals
# 90 or more => A
# between 80 and 89=> B
# between 70 and 79 => C
# between 60 and 69 => D
# 59 or less R

def scoreToLetterGradeOK(score):
    if score >= 90:
        return "A"
    elif score >= 80: #score < 90 and score >= 80
        return "B"
    elif score >= 70:
        return "C"
    elif score >=  60:
        return "D"
    else:
        return "R"


# if conditions are evaluated top to bottom
def scoreToLetterGradeWrong(score):
    if score >= 80:
        return "B"
    elif score >= 90:  # evaluates if score < 80
        return "A"
    elif score >= 70:
        return "C"
    elif score >=  60:
        return "D"
    else:
        return "R"

print(scoreToLetterGrade(95))
