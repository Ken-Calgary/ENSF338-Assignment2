# Time the original code and your improved version, for all integers between 0 and 35,
# and plot the results.
import time
import matplotlib.pyplot as plt

prev_result = {}

def improved_func(n):
    if n == 0 or n == 1:
        return n
    
    if n not in prev_result:
        prev_result[n] = improved_func(n - 1) + improved_func(n -2)
    
    return prev_result[n]

def func(n):
    if n == 0 or n == 1:
        return n
    else: 
        return func(n - 1) + func (n -2)

if "__main__" == __name__:
    time_original = []
    time_improved = []
    for i in range (0, 36):
        time_start = time.perf_counter()
        func(i)
        time_stop = time.perf_counter()
        time_original.append(time_stop - time_start)
    
    for i in range (0, 36):
        time_start = time.perf_counter()
        improved_func(i)
        time_stop = time.perf_counter()
        time_improved.append(time_stop - time_start)

    plt.figure(figsize=(10,3))

    # Plot for Original
    plt.subplot(2,1,1)
    plt.plot(range(0,36), time_original)
    plt.xticks(range(0,36))
    plt.title("Original Function")
    plt.xlabel("nth Fibonacchi Series")
    plt.ylabel("Time To Compute")
    plt.subplot(2,1,2)
    plt.plot(range(0,36), time_improved)
    plt.xticks(range(0,36))
    plt.title("Updated Function Using Memoization")
    plt.xlabel("nth Fibonacchi Series")
    plt.ylabel("Time to Compute")
    plt.show()