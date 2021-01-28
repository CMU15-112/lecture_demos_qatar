def f(x):
    
    if x > 5:
        print("Yep, that is a big number!")
        print("Another line")
    else:
        print("That is a small number")
        
    print("Thanks for calling me.")
    
#f(4)
#f(6)
    
def g(x, y):
# This works, but the psycopath will come for you...
#     if x > 5:
#         if y > 5:
#             print("Both numbers are big!")

    if x > 5 and y > 5:
        print("Both numbers are big!")        
    if x > 5 or y > 5:
        print("At least one of the two numbers is big!")

# g(1,2)
# print("------")
# g(6,2)
# print("------")
# g(6,7)
# print("------")

# def scoreToLetterGrade(score):
#     if score>= 90:
#         return "A"
# 
#     if score >= 80 and score < 90:
#         return "B"
#     
#     if score >= 70 and score < 80:
#         return "C"

def scoreToLetterGrade(score):
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