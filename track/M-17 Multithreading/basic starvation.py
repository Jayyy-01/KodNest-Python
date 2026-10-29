import threading
import time
import heapq

lock = threading.Lock()
queue = []        # min-heap: lower number = higher priority
counter = 0       # keeps arrival order for ties

def join_queue(name, priority):
    global counter
    with lock:
        heapq.heappush(queue, (priority, counter, name))
        counter += 1

def special_guests():
    # a new VIP (priority 0) arrives every second
    for i in range(1, 7):
        join_queue(f"Special Guest {i}", 0)
        print(f"-> Special Guest {i} arrived")
        time.sleep(1)

def kitchen():
    time.sleep(0.5)
    for round_no in range(1, 7):
        with lock:
            if queue:
                _, _, name = heapq.heappop(queue)   # highest priority first
                print(f"Round {round_no}: Food served to {name}. Food over!")
        print("   You: still waiting...")
        time.sleep(1)

# You join with normal (lower) priority
join_queue("You", 1)
print("-> You joined the queue")

t1 = threading.Thread(target=special_guests)
t2 = threading.Thread(target=kitchen)
t1.start()
t2.start()
t1.join()
t2.join()

print("\nProgram ended. 'You' were never served = STARVATION")