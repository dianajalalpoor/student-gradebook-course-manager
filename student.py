class Student:
    def __init__(self, student_id, name, email):
        self.student_id = student_id
        self.name = name
        self.set_email(email)
        self.courses = []


    def get_id(self):
        return self.student_id
    

    def get_name(self):
        return self.name


    def set_email(self, email):
        if "@" in email and "." in email:
            self.email = email

        else:
            print("invalid email!")
        
    def enroll_course(self, course_code):
        if course_code not in self.courses:
            self.courses.append(course_code)


    def display_info(self):
        print("Student_id:", self.student_id)
        print("Name:", self.name)
        print("Email:", self.email)
        print("Courses:", self.courses)


