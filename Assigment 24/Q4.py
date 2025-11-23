import threading
import time
import random

buffer = []
buffer_size = 5

condition = threading.Condition()

def producer(name):
    while True:
        item = random.randint(1, 100)

        with condition:
            while len(buffer) == buffer_size:
                print(f"{name}: Buffer full, waiting...")
                condition.wait()

            buffer.append(item)
            print(f"{name} produced: {item} | Buffer: {buffer}")

            condition.notify_all()

        time.sleep(random.uniform(0.5, 1.5))

def consumer(name):
    while True:
        with condition:
            while len(buffer) == 0:
                print(f"{name}: Buffer empty, waiting...")
                condition.wait()

            item = buffer.pop(0)
            print(f"{name} consumed: {item} | Buffer: {buffer}")

            condition.notify_all()

        time.sleep(random.uniform(0.5, 1.5))


p1 = threading.Thread(target=producer, args=("Producer-1",))
p2 = threading.Thread(target=producer, args=("Producer-2",))


c1 = threading.Thread(target=consumer, args=("Consumer-1",))
c2 = threading.Thread(target=consumer, args=("Consumer-2",))
p1.start()
p2.start()
c1.start()
c2.start()
