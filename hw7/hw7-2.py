# Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

import random
from collections import deque

SIZE = 10
MIN_ITEM = 0.0
MAX_ITEM = 49.0

array = [random.uniform(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)


def merge_array(l: deque, r: deque):
    res = deque()
    while l and r:
        a = l.pop()
        b = r.pop()
        if a > b:
            res.append(b)
            res.append(a)
        else:
            res.append(a)
            res.append(b)
    return res


def split(a: array):
    if len(a) % 2 == 0:
        l = deque(array[0: int(len(a) / 2)])
        r = deque(array[int(len(a) / 2): len(a)])
    else:
        l = deque(array[0: int(len(a) / 2 - 0.5)])
        r = deque(array[int(len(a) / 2 + 0.5): len(a)])
    return l, r


def sort_array(a: array):
    l,r = split(a)


print(merge_array(left, right))


