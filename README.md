# student-gradebook-course-manager

Full name
Diana Jalapoor

project title
Student Gradebook and Course manager

Project describtion
This project is a student gradebook manager developed in python. It allows users to add, view, ubdate, search and delete student, add assessment, record grades and view student repotrts.

How to run the project
Run the (main.py) file and use the menu in the terminal to accsess the projet feature.

classes created
- Student
- Course
- Assessment
- Quiz
- Exam
- Project
- Gradebook

Encapsulation
I used encapsulation in the course class by making course information private and accessing it through getter methods. I also used the set_email() method in the student class to validate email addresses befor ubdating them.

Inheritance
The Quiz, Exam and project classes inherit from the Assessment class.

Method overriding
The Quiz, exam, and Project classess override the grade_message() method to display different messages based on assessmet type.

custom features
1. Dashboard
Display the total number of students, courses and assessments.

2. Letter grade
Convert student's average scores intio letere grades.