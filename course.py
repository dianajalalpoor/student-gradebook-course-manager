class Course:
    def __init__(self, course_code, course_name):
        self.__course_code = course_code
        self.__course_name = course_name
        self.__students = []
        self.__assessments = []


    def get_course_code(self):
        return self.__course_code
    

    def get_course_name(self):
        return self.__course_name
    

    def add_student(self, student_id):
        if student_id not in self.__students:
            self.__students.append(student_id)


    def get_students(self):
        return self.__students
    
    
    def remove_student(self, student_id):
        if student_id in self.__students:
            self.__students.remove(student_id)
            

    def add_assessment(self, assessment):
        self.__assessments.append(assessment)


    def find_assessment(self, title):
        for assessment in self.__assessments:
            if assessment.title == title:
                return assessment
        
        print("Not found")
        return None


    def display_info(self):
        print("Course code:", self.__course_code)
        print("course name:", self.__course_name)
        print("Enrolled student:", len(self.__students))
        print("assessments:")
        for assessment in self.__assessments:
            print("-", assessment.title, "/ Max Score:", assessment.max_score)

