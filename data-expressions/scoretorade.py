def scoreToGrade(n):
    # 90 or more => A
    # between 80 and 89=> B
    # between 70 and 79 => C
    # between 60 and 69 => D
    # 59 or less R
    if n >= 90:
        return "A"
    elif n >= 80:  # if n<90
        return "B"
    elif n>= 70:   #if n<90, n<80
        return "C"
    elif n>=60:
        return "D"
    else:  #
        return "R"


def scoreToGrade2(n):
    # 90 or more => A
    # between 80 and 89=> B
    # between 70 and 79 => C
    # between 60 and 69 => D
    # 59 or less R
    if n >= 90:
        return "A"
    if n >= 80:  # if n<90
        return "B"
    if n>= 70:   #if n<90, n<80
        return "C"
    if n>=60:
        return "D"
    return "R"
