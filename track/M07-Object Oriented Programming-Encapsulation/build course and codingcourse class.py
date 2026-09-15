class Course:
    def __init__(self, course_name):
        self.course_name = course_name    # here course_name is an instance variable 

    def display_course(self):
        print(f"Course: {self.course_name}")


class CodingCourse(Course):     # CodingCourse is a subclass of Course
    pass   


course_name = input().strip()       #taking the input from the user 

# Create a CodingCourse object and display the course
c = CodingCourse(course_name)       #creating the object of CodingCourse class 
c.display_course()      #calling the display_course method