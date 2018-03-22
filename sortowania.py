import time
import random


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
    sorted = 0
    while not sorted:
        sorted = 1
        for i in range(len(dane) - 1):
            if dane[i] > dane[i + 1]:
                dane[i], dane[i + 1] = dane[i + 1], dane[i]
                sorted = 0
    return dane


# quick sort

def porzadkowanie(dane, l, r):
    indexPodzialu = wybierzpunkt(l, r)
    wartoscPodzialu = dane[indexPodzialu]
    print(wartoscPodzialu)
    dane[indexPodzialu], dane[r] = dane[r], dane[indexPodzialu]
    koniec = r
    r -= 1
    while r >= l:
        if dane[r] <= wartoscPodzialu:
            if dane[l] >= wartoscPodzialu:
                dane[l], dane[r] = dane[r], dane[l]
                l += 1
                r -= 1
                print("zmienione ", dane)
            else:
                l += 1
        else:
            r -= 1
    dane[l], dane[koniec] = dane[koniec], dane[l]

    print("posortowane", dane)
    return l


def quick_sort(dane, l, r):
    if l < r:
        x = porzadkowanie(dane, l, r)
        quick_sort(dane, l, x - 1)
        quick_sort(dane, x + 1, r)
    return dane


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
    start_time = time.time()
    dane = bubble_sort(dane)
    print(dane)
    return time.time() - start_time


def gen_list(size, ran):
    lista = []
    lista = [random.randint(0, ran) for x in range(size)]
    return lista


run()
