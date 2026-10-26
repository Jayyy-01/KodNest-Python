from threading import Thread
import time
class Numbers(Thread):
    def run(self):
        for i in range(1,6):
            print(i)
            time.sleep(1)           #means here after one number is printed it will wait for 1 sec then print next number
class Alphabets(Thread):
    def run(self):
        for i in range(ord('a'),ord('f')):
            print(chr(i))
            time.sleep(1)
 
t1 = Numbers()
t2 = Alphabets()

# t1.run()
# t2.run()      

t1.start()
t2.start()

#summary is here, we are printing numbers and alphabets,
#here only one thread is running at a time, 
#and also we have to pass thread objects t1,t2 to start() method not to run() method
#we should not use run() method to start the thread, we should use start() method to start the thread because start() method will create a new thread and run the run() method in that thread
