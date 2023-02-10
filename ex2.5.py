import sys
import json

file = open("ex2.json")
unsorted_lists = json.load(file)
reorganized_lists = []
reorganized_list = []

sys.setrecursionlimit(20000)

def func1(arr, low, high):
    middle = func2(arr, low, high)
    if low <= (middle - 1):
        func1(arr, low, middle - 1)
    if high >= (middle + 1):
        func1(arr, middle + 1, high)


def func2(array, start, end):
    middle_index = int((end - start) / 2) + start
    reorganized_list.append(array[middle_index])
    return middle_index


if __name__ == "__main__":
    for list in unsorted_lists:
        reorganized_list = []
        func1(list, 0, len(list) - 1)
        reorganized_lists.append(reorganized_list)

    with open("ex2.5.json", "w") as write_file:
        json.dump(reorganized_lists, write_file)
