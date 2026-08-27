class TrainingBatch:
    platform_name = "KodNest"
    batch_name = "Python Batch 1"

    def __init__(self,student_name,score):
        self.student_name = student_name
        self.score = score

student1_name = input().strip()
student1_score = float(input())
student2_name = input().strip()
student2_score = float(input())

#create 2 objects
t1 = TrainingBatch(student1_name,student1_score)   #t1 is refrence variable, student1_name and student1_score are local variables
t2 = TrainingBatch(student2_name,student2_score)   #t2 is refrence variable, student2_name and student2_score are local variables

#print shared batch info
print(f"Platform: {TrainingBatch.platform_name}")   #platform_name is class variable so i'm accessing through class name
print(f"Batch: {TrainingBatch.batch_name}")         #batch_name is class variable so i'm accessing through class name

#print the info of both students
print(f"Student 1: {t1.student_name}, Score: {t1.score}")   #student_name and score are instance variables so i'm accessing through object name
print(f"Student 2: {t2.student_name}, Score: {t2.score}")   #student_name and score are instance variables so i'm accessing through object name