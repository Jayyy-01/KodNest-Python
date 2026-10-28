from threading import current_thread
import threading
import time
balance = 1000          #this is resource, shared between the threads t1 and t2, so that i have assigned value to balance in global level, which is shared between t1 and t2
lock = threading.Lock()
def withdraw(amount):
   global balance
   with lock:
      current_balance = balance
      time.sleep(0.1)
      balance = current_balance - amount
      print(f"Thread name = {current_thread().name}, Balance after withdrawal: {balance}")

t1 = threading.Thread(target=withdraw,args=(500,))
t2 = threading.Thread(target=withdraw,args=(300,))

t1.start()
t2.start()

t1.join()
t2.join()

print("Final balance: ",balance)

#summary is here there is a race condition, i.e t1 is about to access t2 might have access to change the value
#so to avoid this we use locks which is in the line 5
#lock is in-built class, so we create an object to the lock class
#lock = lock() so locking is nothing but acquire() and unlocking is nothing but release()
#there are 2 ways to define locks in python
#1. creating lock in class level 
#2. using with lock()