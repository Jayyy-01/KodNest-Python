class StudentProfile:
    def show_profile(self):
        pass        

class FresherStudent(StudentProfile):
    def __init__(self,name,graduation_year):
        self.name = name
        self.graduation_year = graduation_year
    def show_profile(self):
        return f"{self.name} - Fresher - Graduation Year: {self.graduation_year}"
    
class ExperiencedStudent(StudentProfile):
    def __init__(self,name,experience):
        self.name = name
        self.experience = experience
    def show_profile(self):
        return f"{self.name} - Experienced - Experience: {self.experience}"

fresher_name = input().strip()
graduation_year = input().strip()
experienced_name = input().strip()
experience = input().strip()

fresher = FresherStudent(fresher_name,graduation_year)
experienced = ExperiencedStudent(experienced_name,experience)

students = [fresher,experienced]        #creating objects and storing it in the list

for student in students:
    print(student.show_profile())           #calling the show_profile method for each object

        
#summary is here i created base class StudentProfile and i inherited it to FresherStudent and ExperiencedStudent classes
#  in FresherStudent class i __init__ and show_profile method 
#  in ExperiencedStudent class i __init__ and show_profile method 
#  and i used it to create one object and display the object using print(student.show_profile())
#  here both classes are having show_profile method so it is called as polymorphism