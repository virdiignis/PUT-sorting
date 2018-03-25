from time import time
from random import random, choice


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


def quick_sort(data: list) -> list:
    if len(data) <= 1: return data
    dv = choice(data)
    d1, d2 = [x for x in data if x < dv], [x for x in data if x > dv]
    return quick_sort(d1) + [dv] * data.count(dv) + quick_sort(d2)


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
    print("Unsorted list : {}".format(data))
    sorted_data = []
    for j in range(sztosik.size):
        top = sztosik.pop()
        sorted_data.append(top)
    return sorted_data


def gen_list(size: int, ran: int) -> list:
    return [random.randint(0, ran) for _ in range(size)]


if __name__ == "__main__":
    unsorted = gen_list(10, 50)
    print(unsorted)
    start_time = time()
    unsorted = quick_sort(unsorted)
    print(unsorted)
    print(time() - start_time)
