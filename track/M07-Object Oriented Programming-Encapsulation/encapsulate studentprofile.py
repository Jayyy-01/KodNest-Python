class StudentProfile:
    def __init__(
        self,
        student_id,
        name,
        score,
        skills
    ):
        # Create safe private starting values
        # Initialize the properties and skills
        self._student_id = student_id
        self._name = name.strip()
        self._score = score
        self._skills = [skill.strip() for skill in skills if skill.strip()]

    @property
    def student_id(self):
        # Return the read-only student ID
        return self._student_id

    @property
    def name(self):
        # Return the private name
        return self._name

    @name.setter
    def name(self, new_name):
        # Clean and validate the name
        cleaned = new_name.strip()
        if cleaned:
            self._name = cleaned

    @property
    def score(self):
        # Return the private score
        return self._score

    @score.setter
    def score(self, new_score):
        # Accept only scores from 0 to 100
        if 0 <= new_score <= 100:
            self._score = new_score

    @property
    def skills(self):
        # Return a tuple containing the skills
        return tuple(self._skills)

    def add_skill(self, new_skill):
        # Add a cleaned, non-empty and non-duplicate skill
        cleaned = new_skill.strip()
        if cleaned and cleaned not in self._skills:
            self._skills.append(cleaned)

    def __str__(self):
        # Return the complete formatted profile
        skills_str = ", ".join(self._skills)
        return (
            f"STUDENT PROFILE\n"
            f"Student ID: {self._student_id}\n"
            f"Name: {self._name}\n"
            f"Score: {self._score}\n"
            f"Skills: {skills_str}"
        )


student_id = int(input())
name = input().strip()
initial_score = int(input())
skills_input = input().strip()
new_score = int(input())
new_skill = input().strip()

initial_skills = [
    skill.strip()
    for skill in skills_input.split(",")
    if skill.strip()
]

# Create one StudentProfile object
student = StudentProfile(student_id, name, initial_score, initial_skills)

# Update the score through the property
student.score = new_score

# Add the skill through the method
student.add_skill(new_skill)

# Print the final object
print(student)

#Summary : here created class studentprofile and _init_ and @property and @name.setter and @score.setter and @skills.setter and add_skill and __str__ method and i used it to create one object and display the object using print(student)
# and also used it to add skill and update score through property
# i used @property to get and set the score and name and skills
# i used @name.setter to set the name
# i used @score.setter to set the score
# i used @skills.setter to set the skills
