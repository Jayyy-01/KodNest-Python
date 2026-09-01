class Profile:
    def __init__(self, name):    #here i created  _init_ method and i used it to create one object and display the object using print(job)
        self.name = name

    def summary(self):          # here summary method is used to display the summary of the profile
        return f"Name: {self.name}"


class StudentProfile(Profile):    #here i used inheritance 
    def __init__(self, name, course):      # here _init_ method is used to create one object 
        super().__init__(name)      # calling parent class _init_ method
        self.course = course

    # Override summary() here     #i used override to override the summary method of the parent class
    def summary(self):       # here summary method is used to display the summary of the student
        return (
            f"{super().summary()}\n"
            f"Course: {self.course}"
        )


name = input().strip()
course = input().strip()

# Create the object and print its summary
s = StudentProfile(name, course)
print(s.summary())