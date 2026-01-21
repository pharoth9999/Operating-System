import threading
import time
import random

BUFFER_SIZE = 100
buffer = []

# Semaphores
empty = threading.Semaphore(BUFFER_SIZE)  # empty slots
full = threading.Semaphore(0)              # filled slots
mutex = threading.Semaphore(1)             # mutual exclusion


def producer(pid):
    while True:
        # Produce a pair
        p1 = f"P{pid}-1"
        p2 = f"P{pid}-2"

        # Need two empty slots
        empty.acquire()
        empty.acquire()
        mutex.acquire()

        # Place pair consecutively
        buffer.append(p1)
        buffer.append(p2)
        print(f"Producer {pid} produced ({p1}, {p2})")

        mutex.release()
        full.release()
        full.release()

        time.sleep(random.uniform(0.5, 1.5))


def consumer():
    while True:
        # Need two particles
        full.acquire()
        full.acquire()
        mutex.acquire()

        p1 = buffer.pop(0)
        p2 = buffer.pop(0)
        print(f"Consumer packaged ({p1}, {p2})")

        mutex.release()
        empty.release()
        empty.release()

        time.sleep(1)


if __name__ == "__main__":
    producers = []
    for i in range(3):  # multiple producers
        t = threading.Thread(target=producer, args=(i,))
        producers.append(t)
        t.start()

    c = threading.Thread(target=consumer)
    c.start()