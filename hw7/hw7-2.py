# Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

import random

SIZE = 10
MIN_ITEM = 0.0
MAX_ITEM = 49.0

array = [random.uniform(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

if SIZE % 2 == 0:
    left = array[0: int(SIZE / 2)]
    right = array[int(SIZE / 2): SIZE]
else:
    left = array[0: int(SIZE / 2 - 0.5)]
    right = array[int(SIZE / 2 + 0.5): SIZE]
print(left)
print(right)

def sort_m(a: array):
    
