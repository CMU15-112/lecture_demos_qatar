def scoreToGrade(n):
    # 90 or more => A
    # between 80 and 89=> B
    # between 70 and 79 => C
    # between 60 and 69 => D
    # 59 or less R
    if n >= 90:
        return "A"
    elif n >= 80:
        return "B"
    elif n>= 70:
        return "C"
    elif n>=60:
        return "D"
    else:  #
        return "R"

# another way, not good
def scoreToGradeUgly(n):
    # 90 or more => A
    # between 80 and 89=> B
    # between 70 and 79 => C
    # between 60 and 69 => D
    # 59 or less R
    if n >= 90:
        return "A"
    else:
        if n >= 80:
            return "B"
        else:
            if n>= 70:
                return "C"
            else:
                if n>=60:
                    return "D"
                else:  #
                    return "R"

print(scoreToGrade(85))
