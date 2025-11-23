import threading
import time
import string

def print_lowercase():
    for ch in string.ascii_lowercase:  
        print("Lowercase Thread:", ch)
        time.sleep(0.1)  

def print_uppercase():
    for ch in string.ascii_uppercase:   
        print("Uppercase Thread:", ch)
        time.sleep(0.1)


t1 = threading.Thread(target=print_lowercase)
t2 = threading.Thread(target=print_uppercase)

t1.start()
t2.start()

t1.join()
t2.join()

print("Done!")
