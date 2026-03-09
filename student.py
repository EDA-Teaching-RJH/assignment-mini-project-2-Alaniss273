#importing functions from custom 
from grade import calculate_average, assign_letter_grade

#base class
class person:
    def __init__(self, name):
        self.name = name

#student class inherits from person
class Student(Person):
    def __init__(self, student_id, name, grades):
        super().__init__(name)
        self.student_id = student_id
        self.grades = grades

def average(self):
    return calculated_average(self.grades)

def letter_grade(self):
    return assign_letter_grade(self.average())

def display(self):
    return f"{self.student_id} - {self.name} | Avg: {self.average(): .2f} | Grade: {self.letter_grade()}"