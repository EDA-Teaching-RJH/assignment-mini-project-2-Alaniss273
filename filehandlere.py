#This is the file i/o, it reads the strudent's names from the csv file
import csv

def read_students(filenmane):
    students - []
    with open(filename, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            student_id = row[0]
            name = row[1]
            grades = list(map(int, row[2:]))
            students.append((student_id, name, grades))
    return student

#writing the results to the txt file
def write_report(filename, students):
    with open(filename, "w") as file:
        for student in students:
            file.write(student.display() +"\n")