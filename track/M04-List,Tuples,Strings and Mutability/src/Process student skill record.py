skills = []

#read and store 5 skills
for i in range(5):
    skills.append(input()) #as it is string so we are using input()

#convert into tuple
skills = tuple(skills)

#create required slicing

first_three = skills[0:3]
last_two = skills[3:5]
alternative = skills[0:5:2]
reversed = skills[::-1]

print(f"Skill Record: {skills}")
print(f"First three Skills: {first_three}")
print(f"Last two Skills: {last_two}")
print(f"Alternate Skills: {alternative}")
print(f"Reversed Skills: {reversed}")

#Summary: we used slicing concept in tuples to create required slicing
