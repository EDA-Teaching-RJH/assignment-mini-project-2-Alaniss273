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