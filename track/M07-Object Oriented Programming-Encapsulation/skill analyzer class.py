class SkillAnalyzer:
    def __init__(self, student_skills, required_skills):    #here i created _init_ method and i used it to create one object and display the object using print(job)
        self.student_skills = set(student_skills)   # converting the list of skills to a set
        self.required_skills = set(required_skills)

    def get_matched_skills(self):        # get_matched_skills method is used to find the intersection of the two sets
        return self.student_skills & self.required_skills


student_skills = input().split()
required_skills = input().split()

# Create the analyzer and display matched skills
analyzer = SkillAnalyzer(student_skills, required_skills)   #creating the object of SkillAnalyzer class
matched = analyzer.get_matched_skills()   #getting the matched skills

if matched:  #checking if the matched skills are not empty
    print(f"Matched Skills: {', '.join(sorted(matched))}")   #printing the matched skills
else:
    print("Matched Skills: None")   #printing that there are no matched skills

#summary : here i created class SkillAnalyzer and _init_ method and i used it to create one object and display the object using print(job)
# and also used it to get matched skills