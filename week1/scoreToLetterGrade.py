# 
# 90 or more => A
# between 80 and 89 => B
# between 70 and 79 => C
# between 60 and 69 => D
# 59 or less R

def gradeToLetter(courseAverage):
    if courseAverage >= 90:
        return "A"
    elif 80 <= courseAverage < 90:
        return "B"
    elif 70 <= courseAverage < 80:
        return "C"
    elif 60 <= courseAverage < 70:
        return "D"
    else courseAverage:
        return "R"
    
