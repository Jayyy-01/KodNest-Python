class StudentProfile:
    def __init__(self,name,experience,skills):
        self.name = name
        self.experience = experience
        self.skills = skills
    
    def update_experience(self,new_experience):
        self.experience = new_experience
    
    def add_skill(self,new_skill):
        self.skills.append(new_skill)

name = input().strip()
experience = int(input())
skills = input().split()
new_experince = int(input())
new_skill = input().strip()

#create one StudentProfile object
s = StudentProfile(name,experience,skills)
#update the studen's experience
s.update_experience(new_experince) 
#update the student's skill
s.add_skill(new_skill)

print(f"Student Name: {s.name}")
print(f"Updated Experience: {s.experience}")
print(f"Updated Skills: {', '.join(s.skills)}")
    
