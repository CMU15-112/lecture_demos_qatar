def f(x):
    if x > 5:
        print("That is a big number!")
        print("Yep, definately big.")
    else:
        print("That is a small number!")
    print("Bob")

def g(x):
    if x > 5:
        print("That is a big number")
        
    print("Bob")

def scoreToLetterGrade(score):
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
    
print(scoreToLetterGrade(77.4))