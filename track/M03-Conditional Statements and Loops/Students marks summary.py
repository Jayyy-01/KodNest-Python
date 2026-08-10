student_count = int(input())
passed_count = 0
failed_count = 0
total_marks = 0
for i in range(student_count):
    mark = int(input())
    total_marks = total_marks + mark

    if mark >= 40:
        passed_count += 1
    else:
        failed_count += 1

print(f"Total Marks: {total_marks}")
print(f"Passed Count: {passed_count}")
print(f"Failed Count: {failed_count}")

if failed_count == 0:
    print("Batch Result: All Passed")
else:
    print("Batch Result: Needs Improvement")

#summary: using if-else we are able to give the batch result based on the number of passed and failed students
#using for loop we are able to iterate through the list of students and calculate the total marks, passed count, failed count