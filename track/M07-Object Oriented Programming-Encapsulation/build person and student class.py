class Person:
    def display_name(self, name):
        print(f"Student Name: {name}")

        
class Student(Person):
    pass


name = input().strip()

# Create a Student object and call display_name()
s = Student()
s.display_name(name)