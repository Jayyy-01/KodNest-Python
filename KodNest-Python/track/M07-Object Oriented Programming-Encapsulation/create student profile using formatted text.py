class StudentProfile:
    def __init__(self,student_id,name,course,experience):
        self.student_id = student_id
        self.name = name
        self.course = course
        self.experience = experience

    @classmethod
    def from_text(cls,data):
        student_id,name,course,experience = data.split("|")
        return cls(int(student_id),name,course,int(experience))

data = input().strip()
 
student = StudentProfile.from_text(data)    #here from_text is class method so i am calling through class name i.e StudentProfile directly  , not through object i.e student, if i create an object and call it it raises error
print(f"Student ID: {student.student_id}")
print(f"Name: {student.name}")
print(f"Course: {student.course}")
print(f"Experience: {student.experience}")


#class method is used to create object in a different way
#it is called using class name directly, not through object i.e student, if i create an object and call it it raises error
#it takes cls as argument which is class itself i.e StudentProfile
#pass input as 101|jay|py|3 not inside double quotes "101|jay|py|3"