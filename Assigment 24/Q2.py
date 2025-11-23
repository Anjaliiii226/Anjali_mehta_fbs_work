import threading

condition = threading.Condition()
number = 1  

def print_odd():
    global number
    while number <= 10:
        with condition:
            while number % 2 == 0:
                condition.wait()
            print("Odd Thread:", number)
            number += 1
            condition.notify()

def print_even():
    global number
    while number <= 10:
        with condition:
            while number % 2 != 0:
                condition.wait()
            print("Even Thread:", number)
            number += 1
            condition.notify()
t1 = threading.Thread(target=print_odd)
t2 = threading.Thread(target=print_even)

t1.start()
t2.start()

t1.join()
t2.join()

print("Done!")
