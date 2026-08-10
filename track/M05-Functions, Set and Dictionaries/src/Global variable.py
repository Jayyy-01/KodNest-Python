count = 10
def increase():
    global count
    count += 1
    return count
print(increase())