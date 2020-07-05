class analyzer():
    def __init__(self, cname, target_grade, grade_details, db):
        self.cname = cname
        self.total_lost_marks = 0.0
        self.target_grade = target_grade
        self.comment_format = "|{0:^60}|"
        self.total_mark, self.total_weight = db.sum_weight(cname)
        self.total_lost_marks = self.total_weight - self.total_mark
        
    def calculate_grade_needed(self, weight):
        pass

    def comment_component(self, weight, grade): #grade in percent%, weight in percent%
        if grade is None:
            grade_needed = self.calculate_grade_needed(weight)
            print(self.comment_format.format("You need at least {0} percent to achieve your goal.".format(grade_needed)))
        elif grade<self.target_grade:
            lostmark = (100-grade)*weight/100
            print(self.comment_format.format("You have lost {0}% of the total mark in this component.".format(lostmark)))
        else:
            lostmark = (100-grade)*weight/100
            print(self.comment_format.format("You are doing well, you only lost {0} percent in this part.".format(lostmark)))

    def comment_course(self):
        if self.total_lost_marks >= (100-self.target_grade):
            print(" Your goal is unrealistic, you are {0}% behind of your goal.\n".format(self.traget_grade-(100-self.total_lost_marks)))
        else:
            print(" Your goal is achievable, you have lost {0:.3}% of the total grade.".format(self.total_lost_marks))
        print(" Your current average is {0:.3%}.\n".format(self.total_mark/self.total_weight))
