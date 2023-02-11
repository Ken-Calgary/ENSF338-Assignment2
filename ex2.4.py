# Change the code – if possible – to improve its performance on the input given in point 2.

# Test the code on all the inputs at:
# https://raw.githubusercontent.com/ldklab/ensf338w23/main/assignments/assignment2/ex2.json
# Plot timing results.

import sys
import json
import time
from matplotlib import pyplot as plt

file = open("ex2.json")
unsorted_lists = json.load(file)

sys.setrecursionlimit(20000)

def func1(arr, low, high):
    if low < high:
        pi = func2(arr, low, high)
        func1(arr, low, pi-1)
        func1(arr, pi + 1, high)

def func2(array, start, end):
    array[(start + end) // 2], array[start] = array[start], array[(start + end) // 2]
    p = array[start]
    low = start + 1
    high = end
    while True:
        while low <= high and array[high] >= p:
            high = high - 1
        while low <= high and array[low] <= p:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high


if "__main__" == __name__:
    timings = []
    lengths = []

    for list in unsorted_lists:
        time_start = time.perf_counter()
        func1(list, 0, len(list) - 1)
        time_stop = time.perf_counter()
        timings.append(time_stop - time_start)

    for list in unsorted_lists:
        lengths.append(len(list))

    plt.plot(lengths, timings)
    plt.xticks(lengths)
    plt.title("quicksort timing")
    plt.xlabel("number of elements")
    plt.ylabel("Time To Compute")
    plt.show()
