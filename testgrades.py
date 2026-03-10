#import functions to test
from grade import calculate_average, assign_letter_grade, validate_student_id

#test average calculation
def test_average():
    assert calculate_average([80, 90, 100]) == 90

#test letter grade assignment
def test_letter_grade():
    assert assign_letter_grade(85) == "A"
    assert assign_letter_grade(70) == "B"
    assert assign_letter_grade(40) == "E"

#test regex student id validation
def test_valid_id():
    #valid id
    assert validate_student_id("S123") == True
    #invalid id
    assert validate_student_id("123") == False