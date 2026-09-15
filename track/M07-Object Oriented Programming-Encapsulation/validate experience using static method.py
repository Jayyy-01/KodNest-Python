class StudentProfile:
    def __init__(self,name,experience):
        self.name = name
        self.experience = experience

    @staticmethod
    def is_valid_experience(exp):       #it is a static method, which is used to check the experience
        if exp >= 0 and exp <=40:       #checking whether the experience is in between 0 and 40
            return True                 #if it is valid returning True
        return False                    #if it is invalid returning False

name = input().strip()
experience = int(input())

if StudentProfile.is_valid_experience(experience):      #checking experience and printing details only if the experience is valid
    student = StudentProfile(name,experience)           #if exp is valid then only creating object
    print(f"Name: {student.name}")           #printing student name
    print(f"Experience: {student.experience}")       #printing student experience
else:
    print("Invalid experience")         #if exp is invalid then printing invalid experience