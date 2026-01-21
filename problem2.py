import threading
import time

# Semaphores
a = threading.Semaphore(1)  # start allowed
b = threading.Semaphore(0)
c = threading.Semaphore(0)

def process1():
    while True:
        a.acquire()
        print("H", end="")
        print("E", end="")
        b.release()   # allow process2
        b.release()

def process2():
    while True:
        b.acquire()
        print("L", end="")
        c.release()   # allow process3

def process3():
    while True:
        c.acquire()
        c.acquire()
        print("O")

if __name__ == "__main__":
# Threads (representing processes)
    t1 = threading.Thread(target=process1)
    t2 = threading.Thread(target=process2)
    t3 = threading.Thread(target=process3)

    # Start processes
    t1.start()
    t2.start()
    t3.start()

    # Wait for completion
    t1.join()
    t2.join()
    t3.join()