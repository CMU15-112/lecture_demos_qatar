def inClassAverage(quizAverage, exam1Grade, exam2Grade, finalExamGrade):
    return (100* (10*(quizAverage/20)
            + 15*(exam1Grade/100)
            + 15*(exam2Grade/100)
            + 20*(finalExamGrade/100))/60)

print("This is line 7")

q = 12.5
e1 = 61
e2 = 58
f = 80


myInClass = inClassAverage(q, e1, e2, f)

print("My In-Class Average is:", round(myInClass,2))

#print("Result:", myInClass)

