from assessment import Assessment

# Child class of Assessment.
class Quiz(Assessment):

    def display_info(self):
        print("Quiz:", self.title, "-", "Max score:", self.max_score)


    def grade_message(self, score):
        if score >= 8:
            return "Great quiz result"
        
        elif score >= 5:
            return "Good Quiz result"
        
        else:
            return "Needs more practice"
        
    
