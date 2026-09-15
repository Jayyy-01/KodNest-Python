class StudentProfile:
    def __init__(self, student_id,name,course,experience,skills):
        self.student_id = student_id
        self.name = name
        self.course = course
        self.experience = experience
        self.skills = skills

student_id = int(input())
name = input()
course = input()
experience = input()
skills = input().split()

#create one StudentProfile object
student = StudentProfile(student_id,name,course,experience,skills)

#print the data stored in the object
print(f"Student Id: {student.student_id}")
print(f"Name: {student.name}")
print(f"Course: {student.course}")
print(f"Experience: {student.experience}")
print(f"Skills: {', '.join(student.skills)}")
    
    