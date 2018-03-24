from time import time
from random import random, choice


def insertion_sort(dane):
    for index in range(len(dane)):
        i = index - 1
        while dane[index] < dane[i] and i >= 0: i -= 1
        dane.insert(i + 1, dane[index])
        del dane[index + 1]
    return dane


def selection_sort(dane):
    #  XD for x, y in map(lambda i: (i + dane[i:].index(min(dane[i:])), i), range(len(dane))): dane[x], dane[y] = dane[y], dane[x]
    for i in range(len(dane)):
        mini = i + dane[i:].index(min(dane[i:]))
        dane[mini], dane[i] = dane[i], dane[mini]
    return dane


def bubble_sort(dane):
    is_sorted = 0
    while not is_sorted:
        is_sorted = 1
        for i in range(len(dane) - 1):
            if dane[i] > dane[i + 1]:
                dane[i], dane[i + 1] = dane[i + 1], dane[i]
                is_sorted = 0
    return dane


def quick_sort(dane):
    if len(dane) <= 1: return dane
    dv = choice(dane)
    d1, d2 = [x for x in dane if x < dv], [x for x in dane if x > dv]
    return quick_sort(d1) + [dv] * dane.count(dv) + quick_sort(d2)


def wybierzpunkt(l, r):
    return (l + r) // 2


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

    def minindex(self, k):
        if k * 2 + 1 > self.size:
            return k * 2
        elif self.heap[k * 2] < self.heap[k * 2 + 1]:
            return k * 2
        else:
            return k * 2 + 1

    def sink(self, k):
        while k * 2 <= self.size:
            mi = self.minindex(k)
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


def heap_sort(data):
    sztosik = Heap()
    for i in data:
        sztosik.insert(i)
    print("Unsorted list : {}".format(data))
    sorted_data = []
    for j in range(sztosik.size):
        top = sztosik.pop()
        sorted_data.append(top)
    return sorted_data


def merge(a, b):
    # Function to merge two arrays
    c = []
    while len(a) != 0 and len(b) != 0:
        if a[0] < b[0]:
            c.append(a[0])
            a.remove(a[0])
        else:
            c.append(b[0])
            b.remove(b[0])
    if len(a) == 0:
        c += b
    else:
        c += a
    return c


def mergesort(dane):
    if len(dane) <= 1:
        return dane
    return merge(right, left)


def podzial(dane):
    if len(dane) <= 1:
        return dane
    right = podzial(dane[:len(dane) // 2])
    left = podzial(dane[len(dane) // 2:])


def run():
    dane = gen_list(10, 50)
    print(dane)
    start_time = time()
    dane = quick_sort(dane)
    print(dane)
    return time() - start_time


def gen_list(size, ran):
    lista = []
    lista = [random.randint(0, ran) for x in range(size)]
    return lista


run()
