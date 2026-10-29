import threading
import time

pen = threading.Lock()
book = threading.Lock()

def person1():
    with pen:                       # Person 1 grabs the pen
        print("Person 1: I have the pen, waiting for the book...")
        time.sleep(1)               # gives Person 2 time to grab the book
        with book:                  # needs the book too (never gets it)
            print("Person 1: got both, done!")

def person2():
    with book:                      # Person 2 grabs the book
        print("Person 2: I have the book, waiting for the pen...")
        time.sleep(1)
        with pen:                   # needs the pen too (never gets it)
            print("Person 2: got both, done!")

t1 = threading.Thread(target=person1)
t2 = threading.Thread(target=person2)

t1.start()
t2.start()

t1.join()
t2.join()