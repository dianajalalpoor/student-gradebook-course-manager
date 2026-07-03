from assessment import Assessment

# Child class of Assessment
class Project(Assessment):
    
    def display_info(self):
        print("Project:", self.title, "-", "Max score:", self.max_score)


    def grade_message(self, score):
        percentage = self.calculate_percentage(score)
        if percentage >= 80:
            return "Excellent project"
        
        elif percentage >= 60:
            return "Project submitted"
        
        else:
            return "Project needs improvement"
