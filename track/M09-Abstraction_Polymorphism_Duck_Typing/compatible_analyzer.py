from abc import ABC, abstractmethod


class SkillAnalyzer(ABC):
    def __init__(self, student_skills, required_skills):
        self.student_skills = set(student_skills)
        self.required_skills = set(required_skills)

    def get_matched_skills(self):
        return self.student_skills & self.required_skills   #intersection of two sets i.e those skills who matches with the required skills

    @abstractmethod
    def analyze(self):
        pass


class MatchScoreCalculator(SkillAnalyzer):
    def calculate_match_score(self):
        matched = len(self.get_matched_skills())    #gets count of matched skills
        required = len(self.required_skills)        #gets count of required skills
        return matched / required * 100             #match score in percentage

    def analyze(self):
        score = self.calculate_match_score()
        return f"Match Score: {score:.2f}%"     #format string to print match score in percentage


class MissingSkillDetector(SkillAnalyzer):
    def get_missing_skills(self):
        return self.required_skills - self.student_skills #set difference

    def analyze(self):
        missing = sorted(self.get_missing_skills())     #sorts missing skills in ascending order
        if missing:
            return f"Missing Skills: {', '.join(missing)}"  #format string to print missing skills
        return "Missing Skills: None"


class RequiredSkillCountAnalyzer:
    def __init__(self, required_skills):
        self.required_skills = required_skills

    def analyze(self):
        return len(self.required_skills)        #count of required skills


def run_analyzers(analyzers):
    for analyzer in analyzers:
        print(analyzer.analyze())        #calling the analyze method from the objects and analyze() is not defined in SkillAnalyzer class but it is defined in the child classes because ducktyping is used here


student_skills = input().split()      
required_skills = input().split()     

# Create all three analyzers and run them
analyzer1 = MatchScoreCalculator(student_skills, required_skills)   #MatchScoreCalculator object is created
analyzer2 = MissingSkillDetector(student_skills, required_skills)   #MissingSkillDetector object is created
analyzer3 = RequiredSkillCountAnalyzer(required_skills)           #RequiredSkillCountAnalyzer object is created

run_analyzers([analyzer1, analyzer2])                               #calling run_analyzers function with list of analyzer objects

print("Required Skill Count:", analyzer3.analyze())



#summary is here we are using abstraction and polymorphisim 
#like in above problems we are creating a list of objects and iterating through it
#the difference is here we are creating three different types of objects and iterating through it
#the list can contain objects of different classes as long as they have the required methods defined