class StudentProfile:
    def __init__(self, name):
        self.name = name

    def display_profile(self, category):
        print(f"{category}: {self.name}")


class FresherStudent(StudentProfile):
    pass

class ExperiencedStudent(StudentProfile):
    pass


fresher_name = input().strip()
experienced_name = input().strip()

# Create both objects and display their profiles
fresher = FresherStudent(fresher_name)
experienced = ExperiencedStudent(experienced_name)

fresher.display_profile("Fresher Student")
experienced.display_profile("Experienced Student")