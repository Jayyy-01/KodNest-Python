class StudentProfile:
    def __init__(self, student_id, name, course, score = 0.0, skills = None, is_placed = False):
        self.student_id = student_id
        self.name = name
        self.course = course
        self.score = score
        self.skills = [] if skills is None else list(skills) 
        self.is_placed = is_placed
    def __str__(self):
        skills_text = (", ".join(self.skills) if self.skills else "Not Added")
        status_text = ("Placed" if self.is_placed else "Not Placed")
        return(
            f"Student Id: {self.student_id}\n"
            f"Name : {self.name}\n"
            f"Course : {self.course}\n"
            f"Score : {self.score}\n"
            f"Skills : {skills_text}\n"
            f"Placement Status : {status_text}\n"
        )
student = StudentProfile(101, "Jayasree", "Python", 99.9, ["Python", "Frontend", "Backend"], True)
print(student)
