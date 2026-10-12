# with open("student.txt", "x") as file:
#     file.write("Hello Jay")

# # r+ mode
# with open("student.txt", "r+") as file:
#     print(file.read())
#     file.write("Hello")

with open("student.txt", "r+") as file:
    file.seek(0)    #moves the cursor to the 0th position from the beginning 
    file.write("Mango")    #here first 5 characters are replaced with 'Mango', but the remaining characters are still present in the file