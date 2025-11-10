class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"Hi, my name is {self.name} and I am {self.age} years old."

    def __str__(self):
        return self.name
    
    def __eq__(self, other):
        return self.age == other.age
    
    def __gt__(self, other):
        return self.age > other.age
    
    def __lt__(self, other):
        return self.age < other.age    

class Student(Person):
    """
    Inherits from Person.
    """
    def __init__(self, name, age, student_id):
        # Calls the parent class constructor
        super().__init__(name, age)
        self.student_id = student_id
        # Stores grades as a dictionary: {Course object: [list of scores]}
        self.grades = {}

    def introduce(self):
        """
        Overrides the parent method (polymorphism).
        """
        base_intro = super().introduce()
        return f"{base_intro} My student ID is {self.student_id}."


    def enrollInCourse(self, course):
        """Adds a course to the student's record."""
        if course not in self.grades:
            self.grades[course] = 0
            print(f"{self.name} enrolled in {course.name}.")
        else:
            print(f"{self.name} is already enrolled in {course.name}.")
            
    def addGrade(self, course, score):
        """Adds a score for a specific course."""
        if course in self.grades:
            self.grades[course] = score
            print(f"Added score {score} for {course.name}.")
        else:
            print(f"{self.name} is not enrolled in {course.name}.")
            
    def calculateGpa(self):
        """Calculates the average score across all courses."""
        all_scores = [self.grades[crs] for crs in self.grades.keys()]
        print(all_scores)
        if not all_scores:
            return 0.0
        return sum(all_scores)/len(all_scores)

class Course:
    def __init__(self, name, code, instructor):
        self.name = name
        self.code = code
        self.instructor = instructor

    def __str__(self):
        return f"{self.name} ({self.code})"

    def displayInfo(self):
        return f"Course: {self.name} | Code: {self.code} | Instructor: {self.instructor}"




s1 = Student('Adam', 18, 1234)
print(s1.introduce())

c1 = Course("Introduction to Python", "15-112", "Eduardo")
c2 = Course("Algorithms", "15-210", "Mohammad")

s1.enrollInCourse(c1)
s1.enrollInCourse(c2)
s1.addGrade(c1, 85)
s1.addGrade(c1, 95)
s1.addGrade(c2, 100)
print(s1.grades[c1])
for crs in s1.grades:
    print(crs, s1.grades[crs])
print(s1.calculateGpa())
s1.addGrade(c2, 78)
#print(s1.grades)


s2 = Student('Fatima', 18, 1234)

print(s1 < s2)

