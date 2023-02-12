import time

from .draw import draw_list
from .sound import play_note

# from dataclasses import dataclass
# from typing import Callable

# @dataclass
# class AlgorithmInfo:    
#     name: str
#     sort: Callable
#     generator: iter
#     best_case: str
#     average_case: str
#     worst_case: str
#     space_complexity: str


class AlgorithmInfo:
    def __init__(self, name, sort, best_case, average_case, worst_case, space_complexity):
        self.name = name
        self.sort = sort
        #self.generator = generator
        self.best_case = best_case
        self.average_case = average_case
        self.worst_case = worst_case
        self.space_complexity = space_complexity


class PerfInfo:
    def __init__(self):
        self.runtime = 0
        self.start_time = None
        self.operations = 0

    def calc_runtime(self):
        self.runtime = round(time.time() - self.start_time, 3)

def bubble_sort(draw_info, ascending=True):
    lst = draw_info.lst
    
    swapped = True
    passes = 0
    while swapped:
    # for i in range(len(lst) - 1):
        swapped = False
        for j in range(len(lst) - 1 - passes):
            if (ascending and lst[j] > lst[j + 1]) or (not ascending and lst[j] < lst[j + 1]):
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swapped = True
                play_note(lst[j])
                perf_info.operations += 1
                draw_list(draw_info, {j: draw_info.GREEN, j + 1: draw_info.RED}, True)
                yield True # generator - pause and save state until next call
        passes += 1

    return lst


def insertion_sort(draw_info, ascending=True):
    lst = draw_info.lst

    for i in range(1, len(lst)):
        cur = lst[i]

        while True:
            ascending_sort = ascending and i > 0 and lst[i - 1] > cur
            descending_sort = not ascending and i > 0 and lst[i - 1] < cur

            if not ascending_sort and not descending_sort:
                break

            lst[i] = lst[i - 1]
            i = i - 1
            lst[i] = cur

            play_note(lst[i-1])
            perf_info.operations += 1
            draw_list(draw_info, {i - 1: draw_info.GREEN, i: draw_info.RED}, True)
            yield True 

    return lst


def selection_sort(draw_info, ascending=True):
    lst = draw_info.lst
    size = len(lst)

    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):
            # to sort in descending order, change > to < in this line. select the minimum element in each loop
            if ascending and lst[i] < lst[min_idx]:
                min_idx = i
            if not ascending and lst[i] > lst[min_idx]:
                min_idx = i

            play_note(lst[i])
            perf_info.operations += 1
            draw_list(draw_info, {i: draw_info.GREEN, min_idx: draw_info.RED}, True)
            yield True 
                
        # Swap the found minimum element with the first element    
        lst[step], lst[min_idx] = lst[min_idx], lst[step]

    return lst


def shell_sort(draw_info, ascending=True):
    lst = draw_info.lst

    # Rearrange elements at each n/2, n/4, n/8, ... intervals
    n = len(lst)
    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = lst[i]
            j = i
            while (ascending and j >= interval and lst[j - interval] > temp) or (not ascending and j >= interval and lst[j - interval] < temp):
                lst[j] = lst[j - interval]
                j -= interval

            lst[j] = temp

            play_note(lst[i])
            perf_info.operations += 1
            draw_list(draw_info, {i: draw_info.GREEN, j: draw_info.RED}, True)
            yield True 
        interval //= 2

    return lst


def heap_sort(draw_info, ascending=True):
    lst = draw_info.lst

    def max_heapify(arr, n, i):
        largest = i # Initialize largest as root
        l = 2 * i + 1 # left
        r = 2 * i + 2 # right

        if l < n and arr[i] < arr[l]:
            largest = l

        if r < n and arr[largest] < arr[r]:
            largest = r

        # If root is not largest, swap with largest and continue heapifying
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            max_heapify(arr, n, largest)
            play_note(lst[i])
            perf_info.operations += 1
            draw_list(draw_info, {i: draw_info.GREEN, largest: draw_info.RED}, True)

    def min_heapify(arr, n, i):
        smallest = i # Initialize smallest as root
        l = 2 * i + 1 # left
        r = 2 * i + 2 # right
    
        # If left child is smaller than root
        if l < n and arr[l] < arr[smallest]:
            smallest = l
    
        # If right child is smaller than smallest so far
        if r < n and arr[r] < arr[smallest]:
            smallest = r
    
        # If smallest is not root
        if smallest != i:
            arr[i], arr[smallest] = arr[smallest], arr[i]
            # Recursively heapify the affected sub-tree
            min_heapify(arr, n, smallest)
            play_note(lst[i])
            perf_info.operations += 1
            draw_list(draw_info, {i: draw_info.GREEN, smallest: draw_info.RED}, True)

    
    # Build heap
    n = len(lst)
    for i in range(n//2, -1, -1):
        max_heapify(lst, n, i) if ascending else min_heapify(lst, n, i)
        yield True 

    for i in range(n-1, 0, -1):
        lst[i], lst[0] = lst[0], lst[i]
        max_heapify(lst, i, 0) if ascending else min_heapify(lst, i, 0) 
        yield True 

        play_note(lst[i])
        perf_info.operations += 1
        draw_list(draw_info, {i: draw_info.GREEN}, True)
        yield True 

    return lst

bubble_sort_info = AlgorithmInfo("Bubble Sort", bubble_sort, "n", "n^2", "n^2", "1")
selection_sort_info = AlgorithmInfo("Selection Sort", selection_sort, "n^2", "n^2", "n^2", "1")
insertion_sort_info = AlgorithmInfo("Insertion Sort", insertion_sort, "n", "n^2", "n^2", "1")
shell_sort_info = AlgorithmInfo("Shell Sort", shell_sort, "n log n", "n(log n)^2", "n(log n)^2", "1")
heap_sort_info = AlgorithmInfo("Heap Sort", heap_sort, "n log n", "n log n", "n log n", "1")

perf_info = PerfInfo()

# algorithms = {
#     "Bubble Sort" : AlgorithmInfo("Bubble Sort", bubble_sort, None, "n", "n^2", "n^2", "1"),
#     "Selection Sort" : AlgorithmInfo("Selection Sort", selection_sort, None, "n^2", "n^2", "n^2", "1"),
#     "Insertion Sort" : AlgorithmInfo("Insertion Sort", insertion_sort, None, "n", "n^2", "n^2", "1"),
#     "Shell Sort" : AlgorithmInfo("Shell Sort", shell_sort, None, "n log n", "n(log n)^2", "n(log n)^2", "1"),
#     "Heap Sort" : AlgorithmInfo("Heap Sort", heap_sort, None, "n log n", "n log n", "n log n", "1"),
# }
