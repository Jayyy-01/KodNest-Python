class SkillAnalyzer:
    def __init__(self, student_skills, required_skills):
        self.student_skills = set(student_skills)
        self.required_skills = set(required_skills)

    def get_matched_skills(self):
        return self.student_skills & self.required_skills


class MatchScoreCalculator(SkillAnalyzer):
    def calculate_match_score(self):
        # Calculate and return the match percentage
        matched = self.get_matched_skills()
        return (len(matched) / len(self.required_skills)) * 100


class MissingSkillDetector(SkillAnalyzer):
    def get_missing_skills(self):
        # Return the missing skills
        return self.required_skills - self.student_skills


# student_skills = [skill.strip() for skill in input().split(",")]      #taking the input from the user
student_skills = []
for skill in input().split(","):
    student_skills.append(skill.strip())

# required_skills = [skill.strip() for skill in input().split(",")]
required_skills = []
for skill in input().split(","):
    required_skills.append(skill.strip())

calculator = MatchScoreCalculator(student_skills, required_skills)
detector = MissingSkillDetector(student_skills, required_skills)

score = calculator.calculate_match_score()
missing = detector.get_missing_skills()

print(f"{score:.1f}")
if missing:
    print(", ".join(sorted(missing)))
else:
    print("None")


#summary : here i created class SkillAnalyzer and _init_ method and i used it to create one object and display the object using print(job)
# and also used it to find matched skills
# and in MatchScoreCalculator class i created calculate_match_score method and i used it to calculate the match percentage
# and in MissingSkillDetector class i created get_missing_skills method and i used it to find the missing skills