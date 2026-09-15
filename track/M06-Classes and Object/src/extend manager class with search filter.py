# Create the StudentProfile class
class StudentProfile:
    def __init__(self, student_id, name, course):
        self.student_id = student_id
        self.name = name
        self.course = course

    def __str__(self):
        return f"{self.student_id} - {self.name} - {self.course}"


# Create the PlacementManager class
class PlacementManager:
    def __init__(self):
        self.student_profiles = []

    def add_student_profile(self, student_profile):
        self.student_profiles.append(student_profile)

    def filter_students_by_course(self, course):
        matches = []
        for student in self.student_profiles:
            if student.course.lower() == course.lower():
                matches.append(student)
        return matches


manager = PlacementManager()

# Read the student details
n = int(input())

for _ in range(n):
    student_id = int(input())
    name = input().strip()
    course = input().strip()

    student = StudentProfile(student_id, name, course)
    manager.add_student_profile(student)

required_course = input().strip()

# Filter and display the matching students
results = manager.filter_students_by_course(required_course)

if results:
    for student in results:
        print(student)
else:
    print(f"No students found for course: {required_course}")


#summary : here i created manager class and student profile class in student profile class i created 
#  _init_ and __str__ method in manager class i created _init__ and add_student_profile method
#  and filter_students_by_course method and i used it to get the students by course