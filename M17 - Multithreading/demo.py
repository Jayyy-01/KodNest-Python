from threading import *
import time
class Hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello")
            time.sleep(1)

class Hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi")
            time.sleep(1)
        
t1 = Hello() 
t2 = Hi() 

t1.start()
t2.start()

#summary is 
# threads are nothing but lightweight processes
# thread class is used to create threads
# start() method is used to start the thread
# run() method is used to run the thread
# time.sleep() method is used to sleep the thread
# when i run the program it will print hello and hi alternatively
# this is because the threads are running in parallel on different cores
# only one thread can run at a time so one Hello and one Hi at a time
# but we can switch between the threads based on priority, this is called context switching
# this is called multithreading