## Threading is a technique that allows multiple tasksto run simultaneously within a program

import threading
import time
def print_number():
    for i in range(5):
        time.sleep(2)
        print(f'Number: {i}')

def print_letter():
    for letter in "abcde":
        time.sleep(2)
        print(f'Letter: {letter}')

t1 = threading.Thread(target=print_number)
t2 = threading.Thread(target=print_letter)

t = time.time()

#start the thread
t1.start()
t2.start()

#wait for the thread to complete
t1.join()
t2.join()

total_time = time.time() - t
print(f"Total time: {total_time}")
