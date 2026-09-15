class StudentProfile:
    def __init__(self, student_id, name, course, score, is_placed = False):
        self.student_id = student_id
        self.name = name
        self.course = course
        self.score = score
        self.is_placed = is_placed

    def __str__(self):
        # placement_status = "Placed" if self.is_placed else "Not Placed"
        return(
            f"Student Id : {self.student_id}\n"
            f"Name : {self.name}\n"
            f"Course : {self.course}\n"
            f"Score : {self.score}\n"
            f"Placement Status : {status_text}"
        )

student_id = int(input())
name = input().strip()
course = input().strip()
score = float(input())
placement_input = input().strip().lower()

is_placed = False
if placement_input == "yes":
    is_placed = True
    status_text = "Placed"
else:
    status_text = "Not Placed"
    
student = StudentProfile(student_id, name, course, score, is_placed)
print(student)