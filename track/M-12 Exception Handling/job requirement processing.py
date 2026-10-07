try:
    student_exp = int(input())
    required_exp = int(input())
    exp_ratio = student_exp / required_exp
    print(f"Match Ratio: {exp_ratio}")

except ValueError:
    print("Invalid input")
except ZeroDivisionError:
    print("Required experience cannot be zero")