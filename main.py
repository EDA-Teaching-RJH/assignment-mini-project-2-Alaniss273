#import required modules
from student import Student
from filehandler import read_students, write_report
from grade import validate_student_id, validate_name, class_average, top_three_students, bottom_three_students, grade_distribution

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

    
    #creating a menu for a list of questions about the students' grades
    while True:
        print("\n--Student Grade Analyser--")
        print("1. Show all students")
        print("2. Show class average")
        print("3. Show top 3 students")
        print("4. Show bottom 3 students")
        print("5. Show grade distribution")
        print("6. Exit")

        choice = input("Choose an option: ")

        #display each student's information
        if choice == "1":
            for s in students:
                print(s.display())
    
        #class average 
        elif choice == "2":
            avg = class_average(students)
            print(f"\nClass Average: {avg:.2f}")

        #top 3 students 
        elif choice == "3":
            print("\nTop 3 students:")
            for s in top_three_students(students):
                print(s.display())

        #bottom 3 students
        elif choice == "4":
            print("\nBottom 3 students:")
            for s in bottom_three_students(students):
                print(s.display())
    
        #grade distribution
        elif choice == "5":
            distribution = grade_distribution(students)
            print("\nGrade distribution:")
            grades = ["A", "B", "C", "D", "E", "F"]
            for g in grades:
                print(f"{g}: {distribution.get(g, 0)}")

        #exit 
        elif choice == "6":
            print("Exiting...")
            break

        else:
            print("Invalid choice, please try again.")

    #write results to report txt file
    write_report("report.txt", students)

#run program only if this file is executed
if __name__ == "__main__":
    main()