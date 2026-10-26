from threading import Thread,current_thread
import time

class Numbers(Thread):      #creating a thread by passing Thread as parameter to class
    def run(self):
        for i in range(1, 6):
            print(f"Hello from {current_thread().name}")
            print(f"Number: {i}")
            time.sleep(1)  # Pause for 1 second

class Alphabets(Thread):    #creating a thread by passing Thread as parameter to class
    def run(self):
        print(f"Hello from {current_thread().name}")
        for letter in ['A', 'B', 'C', 'D', 'E']:
            print(f"Letter: {letter}")
            time.sleep(1)  # Pause for 1 second


# Start threads
thread1 = Numbers()
thread2 = Alphabets()

thread1.start()
thread2.start()

# Wait for threads to complete
thread1.join()
thread2.join()

print("All tasks are completed!")

#summary is when we use join() method then the threads will run in order, 
#but when we dont use join() method then the threads will run in random order
#also the run method should not be called directly, we should call start() method to start the thread
#because start() method will create a new thread and run the run() method in that thread