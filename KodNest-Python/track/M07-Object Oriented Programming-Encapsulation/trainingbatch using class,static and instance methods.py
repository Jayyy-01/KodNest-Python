class TrainingBatch:
    batch_name = "Python Batch 1"
    student_count = 0

    def __init__(self, student_name, attendance):
        # Store the student data
        self.student_name = student_name
        self.attendance = attendance
        # Increase the shared student count
        TrainingBatch.student_count += 1

    def get_details(self):
        # Return the formatted student details
        return f"{self.student_name}: {self.attendance}%"

    # Create the update_batch_name() class method
    @classmethod
    def update_batch_name(cls, new_name):
        cls.batch_name = new_name

    # Create the is_valid_attendance() static method
    @staticmethod
    def is_valid_attendance(attendance):
        if attendance >= 0 and attendance <= 100:
            return True
        return False


n = int(input())
students = []

# Read n records
# Validate attendance and create valid objects
for _ in range(n):      #reading n inputs
    name = input().strip()
    attendance = int(input().strip())
    if TrainingBatch.is_valid_attendance(attendance):
        students.append(TrainingBatch(name, attendance))

new_batch_name = input().strip()

# Update the shared batch name
TrainingBatch.update_batch_name(new_batch_name)     #calling class method to update the batch name

# Print the batch, count and valid student details
print(f"Batch: {TrainingBatch.batch_name}")
print(f"Valid Students: {TrainingBatch.student_count}")
for student in students:        #iterating through the students list
    print(student.get_details())    #printing the student details

#summary : here i created class TrainingBatch and _init_ method and i used it to create one object and display the object using print(job)
# and also used it to add skill and update score through property
# i used @property to get and set the score and name and skills
# i used @name.setter to set the name
# i used @score.setter to set the score
# i used @skills.setter to set the skills