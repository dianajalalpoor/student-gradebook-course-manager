# parent class 
class Assessment:

    def __init__(self, title, max_score):
        self.title = title
        self.max_score = max_score


    def calculate_percentage(self, score):
        return (score / self.max_score) * 100
    

    def grade_message(self, score):
        if score >= 80:
            return "Exellent!"
        
        elif score >= 50:
            return "good!"
        
        else:
            return "Need more effort!"
        

    def display_info(self):
        print(self.title, "-", "Max score:", self.max_score)
