skills = ["Python", "SQL", "Git", "HTML"]
pos = int(input())

try:
    pos = int(pos)
    print(skills[pos])
except ValueError:
    print("Invalid position")
except IndexError:
    print("Skill not found")