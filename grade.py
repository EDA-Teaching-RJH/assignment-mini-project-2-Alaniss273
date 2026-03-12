#importing regex 
import re

#validating student ids
def validate_student_id(student_id):
    pattern = r"^S\d{3}$"
    return re.match(pattern, student_id)is not None

#validating student names
def validate_name(name):
    pattern = r"^[A-Za-Z ]+$"
    return (pattern, name) is not None

#calculating the average score
def calculate_average(grades):
    return sum(grades) / len(grades)

#converting score to letter grade
def assign_letter_grade(avg):
    if avg >= 85:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 50:
        return "D"
    elif avg >= 40:
        return "E"
    else:
        return "F"
    
def class_average(students):
    if not students:
        return 0
    total = sum(s.average() for s in students)
    return total / len(students)

#using lambda to tell the function sorted() to sort students by the average score
def top_three_students(students):
    sorted_students = sorted(students, key=lambda s: s.average(), reverse=True)
    return sorted_students[:3]

#sorts students by the average grade lowest to highest
def bottom_three_students(students):
    sorted_students = sorted(students, key=lambda s: s.average())
    return sorted_students[:3]

#calculating how many students got the same grade
def grade_distribution(student):
    distribution = {}
    for s in student:
        grade = s.letter_grade()
        if grade in distribution:
            distribution[grade] += 1
        else:
            distribution[grade] = 1
    return distribution

#creating a histogram to visually show how many students got the same grade
def print_histogram(distribution):
    print("\nGrade Distribution Histogram:")
    for grade, count in distribution.items():
        stars = "*" * count 
        print (f"{grade}: {stars} ({count})")