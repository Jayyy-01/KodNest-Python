def add_student(name, students=[]):
    students.append(name)
    print(students)

first_name = input()
second_name = input()
third_name = input()

add_student(first_name)
add_student(second_name)
add_student(third_name)


#for set:
# def add_student(name, students=set()):
#     students.add(name)
#     print(students)

# first_name = input()
# second_name = input()
# third_name = input()

# add_student(first_name)
# add_student(second_name)
# add_student(third_name)

#for dict
# def add_student(name, students={}):
#     students[name] = value (eg: 88, 23, 34 etc)
#     print(students)

# first_name = input()
# second_name = input()
# third_name = input()

# add_student(first_name)
# add_student(second_name)
# add_student(third_name)


