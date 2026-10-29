import threading

name = input().strip()
experience = int(input())
skill = input().strip()

def process_profile():
    print(f"Student profile ready: {name} ({experience} years, {skill})")

# creating thread for process_profile()
thread = threading.Thread(target=process_profile)

#start the thread
thread.start()

# waiting for thread to finish
thread.join()

