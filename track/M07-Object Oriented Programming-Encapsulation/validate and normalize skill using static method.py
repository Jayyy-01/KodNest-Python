class StudentProfile:
    @staticmethod
    def is_valid_skill(skill_name): #checking if the skill name is valid and it is a static method because it is not using any instance variables
        if skill_name.strip() == "": #checking if the skill name is empty because if it is empty then it is not a valid skill
            return False
        for char in skill_name: #iterating through the skill name
            if not (char.isalpha() or char == " "): #checking if not(char is alpha or char is space) then return false
                return False
        return True

    @staticmethod
    def normalize_skill(skill_name): #method to normalize the skill name
        cleaned = skill_name.strip().lower()
        words = cleaned.split()  # splits on any amount of whitespace
        return "_".join(words)


skill_name = input()

# Validate the skill
is_valid = StudentProfile.is_valid_skill(skill_name)

# Normalize and print it only when valid
if is_valid:
    print("Valid skill")
    print(StudentProfile.normalize_skill(skill_name))
else:
    print("Invalid skill")

#summary : here i created class Studentprofile and _init_ method and i used it to create one object and display the object using print(job)
# and also used it to add skill and update score through property
# i used @property to get and set the score and name and skills
# i used @name.setter to set the name
# i used @score.setter to set the score
# i used @skills.setter to set the skills