number_count = int(input())     #taking range from user
p_count = 0
n_count = 0
z_count = 0
total = 0

for i in range(number_count):
    num = int(input())  #reading the actual numbers
    total += num
    if num > 0:
        p_count += 1
    elif num < 0:
        n_count += 1
    else:
        z_count += 1

print(f"Positive Count: {p_count}")
print(f"Negative Count: {n_count}")
print(f"Zero Count: {z_count}")
print(f"Total Sum: {total}")