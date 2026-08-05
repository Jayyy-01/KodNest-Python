marks = int(input())
attendance = int(input())
project_completion = input()

if (marks >= 60 and marks <= 100) and (attendance >= 75 and attendance <= 100):
    if project_completion == "yes":
        print("Eligible")
    else:
        print("Not Eligible")
else:
    print("Not Eligible")