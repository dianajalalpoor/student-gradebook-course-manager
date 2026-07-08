# Control the whole application and connects students, course, assessment, and grades
from student import Student
from course import Course


class Gradebook:
    def __init__(self, passing_grade):
        self.students = {}
        self.courses = {}
        self.grades = {}
        self.passing_grade = passing_grade
    
    def add_student(self, student):
        self.students[student.student_id] = student  


    def add_course(self, course):      
        self.courses[course.get_course_code()]= course  


    def enroll_student(self, student_id, course_code):
        if student_id in self.students and course_code in self.courses:
            course = self.courses[course_code]
            student = self.students[student_id]

            course.add_student(student_id)
            student.enroll_course(course_code)

        else:
            print("Student ID or course code not found")

    def add_assessment(self, course_code, assessment):
        if course_code in self.courses:
            course = self.courses[course_code]
            course.add_assessment(assessment)               


    def record_grade(self, student_id, course_code, assessment_title, score):
        if student_id in self.students and course_code in self.courses:
            course = self.courses[course_code]
            assessment = course.find_assessment(assessment_title)

            if assessment:
                if score < 0:
                    print("Grade cannot be negative")
                    return

                if score > assessment.max_score:
                    print("Grade cannot be higher than maximum score")
                    return

                if student_id not in self.grades:
                    self.grades[student_id] = {}

                if course_code not in self.grades[student_id]:
                    self.grades[student_id][course_code] = {}

                self.grades[student_id][course_code][assessment_title] = score
                print("Grade record successfuly")

            else:
                print("Assessment not found")   

        else:
            print("Student ID or course code not found")        

    
    def calculate_average(self, student_id, course_code):
        if student_id in self.students and course_code in self.courses:
            assessments = self.grades[student_id][course_code]
            course = self.courses[course_code]

            total = 0

            for title, score in assessments.items():
                assessment = course.find_assessment(title)
                percentage = (score / assessment.max_score) * 100
                total += percentage

            return total / len(assessments)
        
        return 0
      

    def show_report(self, student_id):
        if student_id in self.students:
            student = self.students[student_id]

            if student_id in self.grades:
                grades = self.grades[student_id]
            else:
                grades = {}

            print("==================================")
            print("          Student Report         ")
            print("==================================")

            print("Student ID:", student_id)
            print("Student Name:", student.name)
            print("Email:", student.email)

            for course_code in grades:
                course = self.courses[course_code]
                print(f"course: {course.get_course_code()} - {course.get_course_name()}")

                course_grades = grades[course_code]

                for assessment, score in course_grades.items():
                    assessment_obj = self.courses[course_code].find_assessment(assessment)
                    percentage = (score / assessment_obj.max_score) * 100
                    print(f"{assessment}: {score}/{assessment_obj.max_score} = {percentage:.0f}%")

                average = self.calculate_average(student_id, course_code)
                print(f"Average: {average:.2f}%")

                letter = self.get_letter_grade(average)
                print("Leetter grade:", letter)
               
                if average >= self.passing_grade:
                    print("Result: Passed")
                else:
                    print("Result: Failed")


    def search_student(self, keyword):
        for student_id, student in self.students.items():

            if student_id == keyword or student.name.lower() == keyword.lower():
                print("Found:", student.name, "-", student_id)
                return student

        print("Student not found")        
        return None


    def delete_student(self, student_id):
        if student_id in self.students:
            for course in self.courses.values():
                course.remove_student(student_id)
            if student_id in self.grades:
                del self.grades[student_id]

            del self.students[student_id]

            print("Student deleted successfully")

        else:
            print("Student not found")

    # Creative feacher - Dashboard: show total students, courses and assessment.
    def show_dashboard(self):
        print("------Dashbord------")
        print("Total student:", len(self.students))
        print("Total course:", len(self.courses))

        total_assessment = 0

        for course in self.courses.values():
            total_assessment += course.get_assessment_count()
        print("Total assessments:", total_assessment)


    # reative feacher - Leeter grade: Converts average scores into A, B, C, D and F.
    def get_letter_grade(self, average):
        if average >= 90:
            return "A"
        
        elif average >= 80:
            return "B"
        
        elif average >= 70:
            return "C"
        
        elif average >= 60:
            return "D"
        
        else:
            return "F"
        

    def get_result(self, average):
        if average >= self.passing_grade:
            return "Passed"
        
        else:
            return "Failed"

