from time import time
from random import choice, randint
from types import FunctionType


def insertion_sort(data: list) -> list:
    for index in range(len(data)):
        i = index - 1
        while data[index] < data[i] and i >= 0: i -= 1
        data.insert(i + 1, data[index])
        del data[index + 1]
    return data


def selection_sort(data: list) -> list:
    #  XD for x, y in map(lambda i: (i + data[i:].index(min(data[i:])), i), range(len(data))):
    #       data[x], data[y] = data[y], data[x]
    for i in range(len(data)):
        mini = i + data[i:].index(min(data[i:]))
        data[mini], data[i] = data[i], data[mini]
    return data


def bubble_sort(data: list) -> list:
    is_sorted = 0
    while not is_sorted:
        is_sorted = 1
        for i in range(len(data) - 1):
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
                is_sorted = 0
    return data


def quick(data: list, elem_choice: FunctionType) -> list:
    if len(data) <= 1: return data
    dv = elem_choice(data)
    d1, d2 = [x for x in data if x < dv], [x for x in data if x > dv]
    return quick(d1, elem_choice) + [dv] * data.count(dv) + quick(d2, elem_choice)


def quick_sort_random(data: list) -> list:
    return quick(data, choice)


def quick_sort_left(data: list) -> list:
    return quick(data, lambda x: x[0])


def merge(d1, d2):
    i, j = 0, 0
    ld1, ld2 = len(d1), len(d2)
    while i < ld1 and j < ld2:
        if d1[i] < d2[j]:
            yield d1[i]
            i += 1
        else:
            yield d2[j]
            j += 1
    if i < len(d1):
        for x in d1[i:]: yield x
    elif j < len(d2):
        for x in d2[j:]: yield x


def merge_sort(data):
    i = 2
    while i < len(data) * 2:
        for j in range(0, len(data), i):
            data[j:j + i] = merge(data[j:j + i // 2], data[j + i // 2:j + i])
        i *= 2
    return data

# heap sort


class Heap:
    def __init__(self):
        self.heap = [0]
        self.size = 0

    def float(self, k):
        while k // 2 > 0:
            if self.heap[k] < self.heap[k // 2]:
                self.heap[k], self.heap[k // 2] = self.heap[k // 2], self.heap[k]
            k //= 2

    def insert(self, item):
        self.heap.append(item)
        self.size += 1
        self.float(self.size)

    def min_index(self, k):
        if k * 2 + 1 > self.size:
            return k * 2
        elif self.heap[k * 2] < self.heap[k * 2 + 1]:
            return k * 2
        else:
            return k * 2 + 1

    def sink(self, k):
        while k * 2 <= self.size:
            mi = self.min_index(k)
            if self.heap[k] > self.heap[mi]:
                self.heap[k], self.heap[mi] = self.heap[mi], self.heap[k]
            k = mi

    def pop(self):
        item = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.size -= 1
        self.heap.pop()
        self.sink(1)
        return item


def heap_sort(data: list) -> list:
    sztosik = Heap()
    for i in data:
        sztosik.insert(i)
    sorted_data = []
    for j in range(sztosik.size):
        top = sztosik.pop()
        sorted_data.append(top)
    return sorted_data


def counting_sort(data: list, bound: int) -> list:
    cnt = [0] * (bound + 1)
    for i in data: cnt[i] += 1
    ret = []
    for i in range(bound): ret.extend([i] * cnt[i])
    return ret


def gen_list(size: int, ran: int) -> list:
    return [randint(0, ran) for _ in range(size)]


def test_sorts():
    slow = (bubble_sort, insertion_sort, selection_sort)
    fast = (merge_sort, quick_sort_random, quick_sort_left, heap_sort)
    counts = (1000, 2500, 5000, 10000, 25000, 50000, 100000, 250000, 500000)

    def test(counts, functions):
        for c in counts:
            unsorted = gen_list(c, c)
            print("\n{} elements-----------------------------------------------------".format(c))
            for f in functions:
                cp = unsorted.copy()
                start_time = time()
                cp = f(cp)
                end_time = time() - start_time
                print("{}:\t{},\t\tsorted correctly: {}".format(f.__name__, end_time, cp == sorted(cp)))

    test(counts[:4], slow + fast)
    test(counts[4:], fast)


if __name__ == "__main__":
    test_sorts()