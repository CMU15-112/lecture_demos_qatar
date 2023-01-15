def scoreToLetterGradeOK(score):
    if score >= 90:
        return "A"
    elif score >= 80: 
        return "B"
    elif score >= 70:
        return "C"
    elif score >=  60:
        return "D"
    else:
        return "R"
def scoreToLetterGradeWrong(score):
    if score >= 90:
        return "A"
    elif score >= 70:  # WRONG!
        return "C"
    elif score >= 80:
        return "B"
    elif score >=  60:
        return "D"
    else:
        return "R"