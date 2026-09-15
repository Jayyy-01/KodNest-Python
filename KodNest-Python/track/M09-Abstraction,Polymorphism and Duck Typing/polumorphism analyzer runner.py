from abc import ABC, abstractmethod


class SkillAnalyzer(ABC):
    def __init__(self, student_skills, required_skills):
        self.student_skills = student_skills
        self.required_skills = required_skills

    @abstractmethod
    def analyze(self):
        pass


class MatchScoreCalculator(SkillAnalyzer):
    def analyze(self):
        matched_count = 0
        for skill in self.required_skills:
            if skill in self.student_skills:
                matched_count = matched_count + 1

        if len(self.required_skills) > 0:
            score = (matched_count / len(self.required_skills)) * 100
        else:
            score = 0

        return f"Match Score: {score:.2f}%"


class MissingSkillDetector(SkillAnalyzer):
    def analyze(self):
        missing = []
        for skill in self.required_skills:
            if skill not in self.student_skills:
                missing.append(skill)

        if len(missing) == 0:
            return "Missing Skills: None"
        else:
            return "Missing Skills: " + ", ".join(missing)


def run_analyzers(analyzers):
    for analyzer in analyzers:
        result = analyzer.analyze()
        print(result)


student_skills = input().split()
required_skills = input().split()

analyzers = []
analyzers.append(MatchScoreCalculator(student_skills, required_skills))
analyzers.append(MissingSkillDetector(student_skills, required_skills))

run_analyzers(analyzers)


#summary is:this prgm analyze the student skills and required skills and returns the match score and missing skills
#this prgm is polymorphic because it uses the same method name 'analyze' for different purposes
#this prgm is abstract because it uses the abstract class 'SkillAnalyzer'
#this prgm is also example for duck typing i.e 'analyze' method is used for different purposes such as calculating match score and missing skills
#there are two child classes MatchScoreCalculator and MissingSkillDetector which are derived from the abstract class SkillAnalyzer
#the output is the match score and missing skills in two seperate lines
#duck typing is nothing but if the object has the method 'analyze' then it is a SkillAnalyzer and it works
#the 'analyze' method in both the classes are doing different things
#this is a good example of polymorphism and abstraction

#in simple words duck typing means if the object has the method 'analyze' then it is a SkillAnalyzer and it works
#the 'analyze' method in both the classes are doing different things
#this is a good example of polymorphism and abstraction