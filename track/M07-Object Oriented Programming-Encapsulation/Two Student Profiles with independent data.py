class StudentProfile:
    def __init__(self,student_id,name,course):
        self.student_id = student_id
        self.name = name
        self.course = course

first_id = int(input())
first_name = input().strip()
first_course = input().strip()

second_id = int(input())
second_name = input().strip()
second_course = input().strip()

#create first student profile object
first = StudentProfile(first_id,first_name,first_course)

#create second student profile object
second = StudentProfile(second_id,second_name,second_course)

#print the details of both students
print("Student 1")
print(f"ID: {first.student_id}")
print(f"Name: {first.name}")
print(f"Course: {first.course}")

print("Student 2")
print(f"ID: {second.student_id}")
print(f"Name: {second.name}")
print(f"Course: {second.course}")

    