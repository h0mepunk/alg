# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

import random

SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

min1 = array[0]
min2 = array[0]

for _ in range(0, SIZE):
    if array[_] < min1:
        min2 = min1
        min1 = array[_]
    _ += 1

# будут равны, если первый элемент массива является минимальным в массиве, в остальных случаях - различны
print(min1, ' ', min2)
