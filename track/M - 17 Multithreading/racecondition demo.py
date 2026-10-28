import threading
import time
balance = 1000
def withdraw(amount):
   global balance
   current_balance = balance
   time.sleep(0.1)
   balance = current_balance - amount

t1 = threading.Thread(target=withdraw,args=(500,))
t2 = threading.Thread(target=withdraw,args=(300,))

t1.start()
t2.start()

t1.join()
t2.join()

print("Final balance: ",balance)