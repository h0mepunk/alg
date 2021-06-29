# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random

SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

min_ = [array[0], 0]
max_ = [array[0], 0]

for _ in range(0, SIZE):
    if array[_] < min_[0]:
        min_ = [array[_], _]
    if array[_] > max_[0]:
        max_ = [array[_], _]
    _ += 1

print(max_, ' ', min_)
sum_ = 0

if min_[1] > max_[1]:
    for _ in range(max_[1] + 1, min_[1]):
        sum_ += array[_]
    _ += 1
elif min_[1] < max_[1]:
    for _ in range(min_[1] + 1, max_[1]):
        sum_ += array[_]
    _ += 1

else:
    print('чисел между ними нету')

print(sum_)
