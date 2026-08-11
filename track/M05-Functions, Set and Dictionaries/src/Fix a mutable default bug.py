def add_task(task, tasks=None):
    if tasks is None:
        tasks = []
    tasks.append(task)
    return tasks

print(add_task("Learn Python"))
print(add_task("Practice Functions"))

#tasks list is created only once when function is defined, so it is shared between function calls
#To fix this, we use tasks=None as default and check if it is None, if so, create a new list
