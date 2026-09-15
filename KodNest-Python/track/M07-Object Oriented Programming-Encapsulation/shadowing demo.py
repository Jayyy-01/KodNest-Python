class StudentProfile:
    profile_count = 0   # class variable

    def __init__(self, name):
        self.name = name
        self.profile_count += 1   # BUG: this shadows, doesn't update the class var!


#solution: change the 7th line as StudentProfile.profile_count += 1    