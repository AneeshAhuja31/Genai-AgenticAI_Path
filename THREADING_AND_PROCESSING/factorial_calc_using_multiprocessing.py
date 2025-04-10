'''
Real-World Example: Multiprocessing for CPU-bound Tasks
Scenario: Factorial Calculation
Factorial calculations, especially for large numbers,
involve significantly computational work. Multiprocessing
can be used to distribute the workload across multiple
CPU cores, improving performance
'''

import multiprocessing
import math
import sys
import time

# Increase the maximum number of digits for integer conversion
sys.set_int_max_str_digits(100000)

# function to compute factorial of a given number

def compute_factorial(number):
    print(f"Computing factorial of {number}")
    result = math.factorial(number)
    print(f"Factorial of {number} is {result}")
    return result

if __name__ == "__main__":
    numbers = [5000,6000,700,8000]

    start_time = time.time()

    ## create a poo of worker processes
    with multiprocessing.Pool() as pool:
        results = pool.map(compute_factorial,numbers)

    total_time = time.time()- start_time
    
    print(f"REsults: {results}")
    print(f"Time taken: {total_time} seconds")