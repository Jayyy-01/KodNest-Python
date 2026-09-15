def student_eligibility(marks, attendance, project_completed):
    if marks >= 60 and attendance >= 75 and project_completed == "yes":
        return "Eligible"
    else:
        return "Not Eligible"

#read student details
marks = int(input())
attendance = int(input())
project_completed = input().strip()

#check eligibility and print
result = student_eligibility(marks, attendance, project_completed)
print(result)


#summary: define a function for eligibility check and call it in main
#this promotes code reusability, readability, and ease of maintenance
#it also makes it easier to test the eligibility logic independently