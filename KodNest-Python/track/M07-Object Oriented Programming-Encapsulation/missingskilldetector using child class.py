class SkillAnalyzer:
    def __init__(self, student_skills, required_skills):
        self.student_skills = set(student_skills)
        self.required_skills = set(required_skills)

    def get_matched_skills(self):
        return self.student_skills & self.required_skills


class MissingSkillDetector(SkillAnalyzer):
    # Add get_missing_skills()
    def get_missing_skills(self):
        return self.required_skills - self.student_skills   #this is used to find the difference of the two sets


student_skills = input().split()  #taking the input from the user
required_skills = input().split()

# Create the detector and display missing skills
detector = MissingSkillDetector(student_skills, required_skills)
missing = detector.get_missing_skills()

if missing:
    print(f"Missing Skills: {', '.join(sorted(missing))}")
else:
    print("Missing Skills: None")

#summary : here i created class SkillAnalyzer and _init_ method and i used it to create one object and display the object using print(job)
# and also used it to get matched skills
# and in MissingSkillDetector class i created get_missing_skills method and i used it to get the missing skills