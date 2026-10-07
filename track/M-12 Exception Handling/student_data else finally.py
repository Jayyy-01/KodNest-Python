exp = input()
try:
    exp = int(exp)
except ValueError:
    print("Invalid input")
else:
    print(f"Experience: {exp}")
finally:
    print("Student processing completed")