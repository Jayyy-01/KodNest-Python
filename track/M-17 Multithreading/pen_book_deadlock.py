import threading
lock1 = threading.Lock()
lock2 = threading.Lock()

def student_a():
    lock1.acquire()
    print("Student A acquired Pen")

    lock2.acquire()
    print("Student A acquired Book")

    lock2.release()
    lock1.release()

def student_b():
    lock2.acquire()
    print("Student B acquired Book")

    lock1.acquire()
    print("Student B acquired Pen")

    lock1.release()
    lock2.release()

t1 = threading.Thread(target=student_a)
t2 = threading.Thread(target=student_b)

t1.start()
t2.start()

t1.join()
t2.join()

#summary is here 1st thread is acquiring in ascending order and 2nd thread is acquiring in descending order
#so deadlock is avoided

#if 1st thread is ascending order and 2nd thread is also ascending order then deadlock will happen
#if 1st thread is descending order and 2nd thread is also descending order then deadlock will happen
#to avoid deadlock we have to acquire the locks in same order, and that is done in 1st student and 2nd student in the line 20 and 28

#and also we can use RLock() to avoid deadlock
#lock is in-built class, so we create an object to the lock class
#lock = lock()

#RLock is nothing but Reentrant Lock, which is nothing but we can acquire the lock multiple times
#eg: if i want to perform multiple operations on the same lock, then we can use RLock