# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

max_ = [array[0], 0]
min_ = [array[0], 0]

for _ in range(0, SIZE):
    if array[_] > max_[0]:
        max_ = [array[_], _]
    if array[_] < min_[0]:
        min_ = [array[_], _]
    _ += 1

array[min_[1]], array[max_[1]] = array[max_[1]], array[min_[1]]

print(array)
