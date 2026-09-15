class StudentProfile:
    @staticmethod
    def normalize_skill(skill_name):
        clean = skill_name.strip().lower()  #strip() is used to remove the spaces and lower() is used to convert the string into lowercase
        clean = "_".join(clean.split())     # here _ is used to join the words and here split() is used to split the string into a words
        return clean


skill_name = input()

# Normalize the skill using the class name
normalized = StudentProfile.normalize_skill(skill_name)

# Print the normalized skill
print(normalized)

#Summary : here created class studentprofile and @staticmethod and normalize_skill method and i used it to normalize the skill name 
# and print the normalized skill