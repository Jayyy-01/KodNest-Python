class StudentProfile:
    def __init__(self,student_id,name,course):
        self.student_id = student_id
        self.name = name
        self.course = course

    def __str__(self):
        return f"{self.student_id} - {self.name} - {self.course}"
    
class PlacementManager:
    def __init__(self):
        self.student_profiles = []
    def add_student_profile(self,student_profile): 
        self.student_profiles.append(student_profile)
    def display_profiles(self):
        if len(self.student_profiles) == 0:
            print("No student profiles found")
        else:
            print("STUDENT PROFILES")
            for profile in self.student_profiles:
                print(profile)

manager = PlacementManager()
n = int(input())
for _ in range(n):
    student_id = input()
    name = input()
    course = input()
    
    studentprofile = StudentProfile(student_id,name,course)
    manager.add_student_profile(studentprofile)
manager.display_profiles()
        