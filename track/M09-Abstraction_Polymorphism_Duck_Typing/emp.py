# class Employee:
#     def __init__(self,name,id,salary,dept):
#         self.name = name
#         self.id = id
#         self.salary = salary
#         self.dept = dept
    
#     if self.id == 1:
#         def __return__(self):
#             return(
#                 f"Name : {self.name}",
#                 f"Id : {self.id}",
#                 f"Salary : {self.salary}",
#                 f"Dept : {self.dept}"
#             )

# name = input("enter employee name: ").strip()
# id = int(input("enter empid: "))
# salary = int(input("enter salary: "))
# dept = input("enter dept: ").strip()

# e = Employee(name,id,salary,dept)
# print(e.name)
# print(e.id)
# print(e.salary)
# print(e.dept)





s = input().strip()
freq = {}
for i in s:
    freq[i] = freq.get(i,0) + 1     # get the value of the key i if it is present then add 1 to it else the default value is 0 and add 1 to it

for i in s:
    if freq[i] > 1:
        print(-1)
        break























    
    
        