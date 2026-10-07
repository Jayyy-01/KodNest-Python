experience = input()
try:
    experience = int(experience)
    print(f"Experience: {experience}")
except ValueError:
    print("Invalid input")