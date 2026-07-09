
from student import Student
from course import Course
from assessment import Assessment
from quiz import Quiz
from exam import Exam
from project import Project
from gradebook import Gradebook

gradebook = Gradebook(55)

student_1 = Student("S001", "manija Shams", "manija@gmail.com")
student_2 = Student("S002", "Hosna Karimi", "hosna@gmail.com")
gradebook.add_student(student_1)
gradebook.add_student(student_2)

course_1 = Course("PY101", "python programing")
gradebook.add_course(course_1)

gradebook.enroll_student("S001", "PY101")
gradebook.enroll_student("S002", "PY101")

continue_menu = True

while continue_menu:
    print("===========================================")
    print("        Student Gradebook manager")
    print("===========================================")

    print("1. Add student")
    print("2. View stuents")
    print("3. Add course")
    print("4. View courses")
    print("5. Enroll student in course")
    print("6. Add assignment")
    print("7. Record grade")
    print("8. View student report")
    print("9. Search student")
    print("10. Delet student")
    print("11. Ubdate student")
    print("12. Dashbord")
    print("0. Exit")


    choice = int(input("Choose an option:\n"))

    if choice == 1:
        new_student = Student("S003", "Sara Ahmadi", "Sara@gmail.com")
        gradebook.add_student(new_student)
        print("Student added successfully")

    elif choice == 2:
        for student in gradebook.students.values():
            student.display_info()        

    elif choice == 3:
        new_course = Course("MATH101", "Math")
        gradebook.add_course(new_course)
        print("Course added successfully")

    elif choice == 4:
        for course in gradebook.courses.values():
            print(course.get_course_code(), "-", course.get_course_name())

    elif choice == 5:
        gradebook.enroll_student("S003", "MATH101")
        print("Student enrolled successfully")

    elif choice == 6:
        quiz = Quiz("Quiz 1", 10)
        gradebook.courses["PY101"].add_assessment(quiz)
        print("Assessment added (Quiz 1)")

    elif choice == 7:
        gradebook.record_grade("S001", "PY101", "Quiz 1", 10)

    elif choice == 8:
        gradebook.show_report("S001")

    elif choice == 9:
        search = input("Enter studnt ID or name: ")
        gradebook.search_student(search)

    elif choice == 10:
        student_id = input("Enter student ID: ")
        gradebook.delete_student(student_id)

    elif choice == 11:
        student_id = input("Enter studend ID: ")
        name = input("Enter new name: ")
        email = input("Enter new email: ")
        gradebook.ubdate_student(student_id, name, email)

    elif choice == 12:
        gradebook.show_dashboard()

    elif choice == 0:
        print("You are exit")
        continue_menu = False

    else:
        print("Invalid option")

