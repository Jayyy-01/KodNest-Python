skill_count = input()
try:
    skill_count = int(skill_count)
    print(f"Skill count: {skill_count}")
except ValueError:
    print("Invalid input") 