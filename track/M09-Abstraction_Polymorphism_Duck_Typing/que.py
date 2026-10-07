li = list(map(int, input("enter: ").split(" ")))
new = {}
for i in li:
    if i not in new:
        new[i] = 1
    else:
        new[i] += 1
for i in new:
    if new[i] == 1:
        print(i)
        break 