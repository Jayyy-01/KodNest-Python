n = int(input())
registrations = set()

for _ in range(n):
    student_id = input().strip()
    registrations.add(student_id)

search_id = input().strip()

unique_count = 0
duplicate_count = 0

duplicate_set = set()

for i in registrations:
    if i not in duplicate_set:
        duplicate_set.add(i)
        unique_count += 1
    else:
        duplicate_count += 1

if search_id in duplicate_set:
    print("Registered")
else:
    print("Not Registered")


print(f"Unique count: {unique_count}")
print(f"Duplicate count: {duplicate_count}")


#summary: registrations is a set() -> entering "ki1" twice, the second one just gets silently dropped, so the loop never even sees the duplicate.
#before counting duplicates, the duplicates are removed from the set, so duplicate count will show wrong
# Result: no error shown, code runs fine, but duplicate_count comes out wrong here.
