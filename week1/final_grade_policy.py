"""
quiz  10%, exam1: 15, exam2: 15, final:20

Final Grade Policy
You must receive a 60% or higher
(calculating using the appropriate weightings above)
on in-class assessments in order to receive a D or higher in the course.

You must receive a 65% or higher
(calculating using the appropriate weightings above)
on in-class assessments in order to receive a C or higher in the course.
I used ChatGPT for my homeworks, and I scored
An average of 12.5 over 20 on quizzes (after dropping lowest two)

61 on Exam 1
58 on Exam 2
62 on the final
Can I get a C? Can I get a D?"""

quizAverage = 12.5
exam1Grade = 61
exam2Grade = 58
finalExamGrade = 80
print(100* (10*(quizAverage/20)
            + 15*(exam1Grade/100)
            + 15*(exam2Grade/100)
            + 20*(finalExamGrade/100))/60)


