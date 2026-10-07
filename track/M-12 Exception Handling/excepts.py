#TypeError
try:
    age = int(input("enter age: "))
    print(f"Your age is: {age}")
except Exception as e:
    print("Invalid age")


#ZeroDivisionError
try:
    matched_skills = 4
    required_skills = 0
    # match_score = matched_skills / required_skills
    # print(match_score)
except ZeroDivisionError:
    print("division error")

#IndexError
skills = ["Python", "Sql", "Git"]
print(skills[5])

#KeyError
student = {"name" : "asha", "age" : 20,}
print(student["skills"])

#TypeError
experience = 2
bonus = "1"
total = experience + bonus
print(total)


#NameError
student_name = "Asha"
# print(student_age)

#AttributeError
student = {"name" : "asha"}
print(student.age)