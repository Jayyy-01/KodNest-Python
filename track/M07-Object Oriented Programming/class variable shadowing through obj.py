class TrainingBatch:
    batch_name = "Python Batch 1"

    def __init__(self,student_name):
        self.student_name = student_name

student1_name = input().strip()
student2_name = input().strip()
special_batch = input().strip()
new_shared_batch = input().strip()

#create 2 TrainingBatch objects
t1 = TrainingBatch(student1_name)
t2 = TrainingBatch(student2_name)

#create obj specific batch value for t1
t1.batch_name = special_batch

#update the shared class variable
TrainingBatch.batch_name = new_shared_batch

print(f"Class Batch: {TrainingBatch.batch_name}")
print(f"{t1.student_name} Batch: {t1.batch_name}")
print(f"{t2.student_name} Batch: {t2.batch_name}")