# Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

import random

SIZE = 9
MIN_ITEM = 0.0
MAX_ITEM = 49.0

array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)
buf = []


def merge_array(l: array, r: array):
    res = []
    while l and r:
        if l[0] > r[0]:
            res.append(r.pop(0))
            res.append(l.pop(0))
        else:
            res.append(l.pop(0))
            res.append(r.pop(0))
    if l:
        res.append(l[0])
    if r:
        res.append(r[0])
    return res


def write_buf_to_a(first: int, num: int):
    for i in range(first, num):
        array[i] = buf.pop(i - num)


def sort_array(a: array, fl: bool, chunk_size: int, first_el):
    if fl == False: # сплиттим
        if chunk_size > 1:
            if chunk_size % 2 == 0:
                chunk_size /= 2
                sort_array(a, False, chunk_size / 2 - 1, first_el)
                sort_array(a, False, chunk_size / 2, chunk_size / 2)
            else:
                sort_array(a, False, chunk_size / 2 - 0.5, first_el)
                sort_array(a, False, chunk_size / 2 + 0.5, chunk_size / 2 - 0.5)
        else:
            if chunk_size % 2 == 0:
                buf = merge_array(a[first_el], a[first_el + 1])
                write_buf_to_a(first_el, 2)
                first_el += 2

            else:
                buf = merge_array(a[first_el: first_el + 1], a[first_el + 3])
                write_buf_to_a(first_el, 3)
                first_el += 3
    else:
        if chunk_size == len(a):
            return a
        else:
            buf = merge_array(a[first_el, chunk_size / 2], a[chunk_size / 2, chunk_size])
            write_buf_to_a(first_el, chunk_size)
            chunk_size *= 2
            first_el += chunk_size













# print(merge_array([1, 4], [7]))

print(sort_array(array))
