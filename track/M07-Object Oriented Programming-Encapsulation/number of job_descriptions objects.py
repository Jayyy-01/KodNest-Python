class JobDescription:
    job_count = 0

    def __init__(self, role, company):
        self.role = role
        self.company = company
        JobDescription.job_count += 1   #here job_count is a class variable and it is incremented by 1 for each object creation and it is accessed through class name

n = int(input())
jobs = []

# Read n job records and create n objects
for _ in range(n):
    role = input()
    company = input()
    job = JobDescription(role, company)
    jobs.append(job)

# Print the total number of created jobs
print(JobDescription.job_count)

#summary : here created class Jobdescription and _init_ method and i used it to create one object and display the object using print(job)
# and also used it to add skill and update score through property
# i used @property to get and set the score and name and skills
# i used @name.setter to set the name
# i used @score.setter to set the score
# i used @skills.setter to set the skills