from assessment import Assessment

# Child class of Assessment
class Exam(Assessment):

    def display_info(self):
        print("Exam:", self.title, "-", "Max score:", self.max_score)


    def grade_message(self, score):
        percentage = self.calculate_percentage(score)
        if percentage >= 55:
            return "Passed exam" 

        else:
            return "Failed exam"   
    