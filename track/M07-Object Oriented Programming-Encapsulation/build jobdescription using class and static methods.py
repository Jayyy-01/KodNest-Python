class JobDescription:
    platform_name = "KodNest Jobs"

    def __init__(
        self,
        role,
        company,
        minimum_experience
    ):
        self.role = role
        self.company = company
        self.minimum_experience = minimum_experience

    # Create the is_valid_experience() static method
    @staticmethod
    def is_valid_experience(experience):    # here @staticmethod is used to create a static method
        if 0<= experience<=20 :  # here 0 <= experience <= 20 is used to check the experience is valid or not
            return True
        return False

    # Create the from_text() class method
    @classmethod
    def from_text(cls, data):
        role, company, experience_str = data.split("|") # here split("|") is used to split the string into a list of strings
        experience = int(experience_str)

        if not cls.is_valid_experience(experience):
            return None

        role = role.strip().title()
        company = company.strip()

        return cls(role, company, experience)


data = input()

# Create the job using from_text()
job = JobDescription.from_text(data)

# Print the job or the invalid message
if job is not None:
    print(f"Platform: {JobDescription.platform_name}")
    print(f"Role: {job.role}")
    print(f"Company: {job.company}")
    print(f"Minimum Experience: {job.minimum_experience}")
else:
    print("Invalid experience value")

#Summary : here created class JobDescription and __init_ and @staticmethod and @classmethod and used it to create one object and display the object using print(job)
# and also used it to add skill and update score through property
# i used @property to get and set the score and name and skills
# i used @name.setter to set the name
# i used @score.setter to set the score
# i used @skills.setter to set the skills
