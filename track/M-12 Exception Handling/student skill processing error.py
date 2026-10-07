try:
    matched_skills = int(input())
    required_skills = int(input())
    matched_per = (matched_skills / required_skills) * 100
    print(f"Match Percentage: {matched_per}")
except ValueError:
    print("Invalid skill count")
except ZeroDivisionError:
    print("Required skills cannot be zero")