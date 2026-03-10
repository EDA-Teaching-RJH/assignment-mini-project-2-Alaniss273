#import required modules
from student import Student
from filehandler import read_students, write_report
from grade import validate_student_id, validate_name

#function to convert CSV data into Students
def create_students(data):
    student_objects = []
    for student_id, name, grades in data:
        try:
            #validate student id using regex
            if not validate_student_id(student_id):
                raise ValueError("Invalid Student ID")
            
            #validate name using regex
            if not validate_name(name):
                raise ValueError("Invalid Name")
            
            student = Student(student_id, name, grades)
            student_objects.append(student)

        #for errors
        except ValueError as e:
            print(f"Error with student {student_id}: {e}")
    return student_objects

#main program function
def main():

    #read student data from CSV file
    data = read_students("students.csv")
    students = create_students(data)

    #display each student's information
    for s in students:
        print(s.display())

    #write results to report txt file
    write_report("report.txt", students)

#run program only if this file is executed
if __name__ == "__main__":
    main()