class StudentProfile:
    profile_count = 0
    def __init__(self, name):
        self.name = name
        StudentProfile.profile_count += 1

n = int(input())
students = []
for _ in range(n):
    name = input().strip()
    student = StudentProfile(name)
    students.append(student)

print(f"Total profiles = {StudentProfile.profile_count}")
