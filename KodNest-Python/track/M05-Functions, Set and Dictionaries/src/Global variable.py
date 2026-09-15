count = 10
def increase():
    global count  #important
    count += 1
    return count
print(increase())   #output: 11

#here if we don't use global keyword then output will be 10

count = 10
def increase():
    # global count
    count += 1
    return count
print(increase())   #output: 10