class StudentProfile:
    def __init__(self, name, initial_score):
        self.name = name
        self.__score = initial_score

    def get_score(self):
        return self.__score

    def set_score(self, new_score):
        if new_score >= 0 and new_score <= 100:
            self.__score = new_score
            return True
        return False


name = input().strip()
initial_score = int(input())
new_score = int(input())

# Create one StudentProfile object
student = StudentProfile(name, initial_score)

# Call set_score() and store its Boolean result
result = student.set_score(new_score)
# Display the update result
if result:
    print("Score Updated")
else:
    print("Invalid Score")

# Display the name and final score
print(f"Name: {student.name}")
print(f"Final Score: {student.get_score()}")

#Summary : here created class studentprofile and _init_ and get_score and set_score method and i used it to update the score
# if the score is updated it will print Score Updated else print Invalid Score
