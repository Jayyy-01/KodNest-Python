n = int(input())
scores = []

for i in range(n):
    val = int(input())
    scores.append(val)
search_score = int(input())
highest_score = max(scores)
lowest_score = min(scores)
total = sum(scores)

print(f"Highest Score: {highest_score}")
print(f"Lowest Score: {lowest_score}")
print(f"Average Score: {total}")

if search_score in scores:
    print("Search Result: Found")
else:
    print("Search Result: Not Found")