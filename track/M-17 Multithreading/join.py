from threading import Thread 
import time

def print_numbers():
    for i in range(1, 6):
        print(f"Number: {i}")
        time.sleep(1)  # Pause for 1 second

def print_letters():
    for letter in ['A', 'B', 'C', 'D', 'E']:
        print(f"Letter: {letter}")
        time.sleep(1)  # Pause for 1 second


# create thread objects
thread1 = Thread(target=print_numbers)
thread2 = Thread(target=print_letters)

#start threads
thread1.start()
thread1.join()
thread2.start()

#wait for threads to complete
thread2.join()

print("All tasks are completed!")

