def calculate_grade_distribution_with_lists(grades):
    unique_grades = []
    grade_frequencies = []
    
    for grade in grades:
        if grade in unique_grades:
            index = unique_grades.index(grade)
            grade_frequencies[index] += 1
        else:
            unique_grades.append(grade)
            grade_frequencies.append(1)
    
    return unique_grades, grade_frequencies

# Example usage:
grades = [85, 90, 75, 85, 95, 90, 80, 85, 90]
unique_grades, grade_frequencies =  calculate_grade_distribution_with_lists(grades)
print(f"unique_grades: {unique_grades} ")
print(f"grade_frequencies: {grade_frequencies} ")

gradesFreq_mapped= list(zip(unique_grades,grade_frequencies))

print("MergedLists:", gradesFreq_mapped)
print()



def calculate_grade_distribution_with_dict(grades):
    grade_distribution = dict()
    for grade in grades:
        if grade in grade_distribution:
            grade_distribution[grade] += 1
        else:
            grade_distribution[grade] = 1
    return grade_distribution

# Example usage:
grades = [85, 90, 75, 85, 95, 90, 80, 85, 90]
print("Dict: ", calculate_grade_distribution_with_dict(grades))







