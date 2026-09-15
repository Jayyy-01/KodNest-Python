limit = int(input())
total = 0
number = 1

while number <= limit:
    if number % 2 == 0:
        total += number
    number = number + 1     #here we are incrementing the number

print(f"Even Sum: {total}")