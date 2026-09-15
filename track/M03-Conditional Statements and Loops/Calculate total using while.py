value = int(input())

count = 1
total = 0

while count <= value:
    total = total + count
    count = count + 1

print(f"Total: {total}")