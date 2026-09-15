class SkillAnalyzer:
    def __init__(self, student_skills, required_skills):
        self.student_skills = set(student_skills)   #converting the list of skills to a set
        self.required_skills = set(required_skills) 

    def get_matched_skills(self):
        return self.student_skills & self.required_skills   #this is used to find the intersection of the two sets


class MatchScoreCalculator(SkillAnalyzer):
    # Add calculate_match_score()
    def calculate_match_score(self):  #here calculate_match_score method is used to calculate the match score
        matched = self.get_matched_skills()
        score = (len(matched) / len(self.required_skills)) * 100     #calculating the match score
        return score


student_skills = input().split()  #taking the input from the user
required_skills = input().split()

# Create the calculator and display the score
calc = MatchScoreCalculator(student_skills, required_skills)
score = calc.calculate_match_score()
print(f"Match Score: {score:.2f}%")

#summary : here i created class SkillAnalyzer and _init_ method and i used it to create one object and display the object using print(job)
# and also used it to get matched skills
# and in MatchScoreCalculator class i created calculate_match_score method and i used it to calculate the match score