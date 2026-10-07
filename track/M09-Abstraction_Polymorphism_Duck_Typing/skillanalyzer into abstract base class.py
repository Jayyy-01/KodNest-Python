from abc import ABC, abstractmethod


class SkillAnalyzer(ABC):
    def __init__(self, student_skills, required_skills):
        self.student_skills = set(student_skills)
        self.required_skills = set(required_skills)

    def get_matched_skills(self):
        return self.student_skills & self.required_skills

    @abstractmethod
    def analyze(self):
        pass


class MatchScoreCalculator(SkillAnalyzer):       #class to calculate the match score
    def calculate_match_score(self):             #method to calculate the match score
        matched = len(self.get_matched_skills())        #checking how many skills are matched
        required = len(self.required_skills)            #checking how many skills are required
        return matched / required * 100           #dividing the matched skills by the required skills and multiplying by 100

    def analyze(self):              #abstract method overridden from the abstract class
        return f"Match Score: {self.calculate_match_score():.2f}%"        #formatted string to display the match score


class MissingSkillDetector(SkillAnalyzer):
    def get_missing_skills(self):           #method to get the missing skills
        return self.required_skills - self.student_skills

    def analyze(self):              #abstract method overridden from the abstract class
        missing = sorted(self.get_missing_skills())  #sorting the missing skills

        if missing:
            return "Missing Skills: " + ", ".join(missing) #joining the missing skills and returning
        else:
            return "Missing Skills: None"


student_skills = input().split()
required_skills = input().split()

score_analyzer = MatchScoreCalculator(student_skills, required_skills)  #creating objects of the classes
missing_analyzer = MissingSkillDetector(student_skills, required_skills)  #creating objects of the classes

print(score_analyzer.analyze())  #displaying the object using print
print(missing_analyzer.analyze())  #displaying the object using print

#summary : here i created abstract class SkillAnalyzer and i used it to create one object and display the object using print(score_analyzer.analyze()) and print(missing_analyzer.analyze())