requirements = ["Python", "SQL", "Git", "REST API"]
pos = input()
try:
    pos = int(pos)
    print(requirements[pos])
except ValueError:
    print("Invalid position")
except IndexError:
    print("Skill not found") 