class JobDescription:
    def __init__(
        self,
        role,
        company,
        minimum_experience,
        required_skills
    ):
        self.role = role
        self.company = company
        self.minimum_experience = minimum_experience
        self.required_skills = required_skills

    # Create the from_text() alternative constructor
    @classmethod
    def from_text(cls, data):
        parts = data.split(";")
        role = parts[0].strip().title()
        company = parts[1].strip()
        minimum_experience = int(parts[2].strip())
        required_skills = [skill.strip() for skill in parts[3:]]
        # if skills were comma-separated within one field:
        if len(required_skills) == 1 and "," in required_skills[0]:
            required_skills = [s.strip() for s in required_skills[0].split(",")]

        return cls(role, company, minimum_experience, required_skills)


data = input()

# Create the JobDescription using from_text()
job = JobDescription.from_text(data)

# Print the stored job information
print(f"Role: {job.role}")
print(f"Company: {job.company}")
print(f"Minimum Experience: {job.minimum_experience}")
print(f"Required Skills: {', '.join(job.required_skills)}")

#summary : here i created class Jobdescription and _init_ method and i used it to create one object and display the object using print(job)
# and also used it to add skill and update score through property
# i used @property to get and set the score and name and skills
# i used @name.setter to set the name
# i used @score.setter to set the score
# i used @skills.setter to set the skills

# this is input:  data ;    analyst; 3;   python,sql, powerbi

# this is output:
# Role: Data
# Company: analyst
# Minimum Experience: 3
# Required Skills: python, sql, powerbi