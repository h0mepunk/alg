# Определить, какое число в массиве встречается чаще всего.

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
# array = [11, 9, 8, 11, 5, 5, 11, 5, 11, 7, 9, 11] - тестовый массив
print(array)
num_of_ = [0]*SIZE

for i in range(0, SIZE):
    for j in range(0, SIZE):
        if array[i] == array[j]:
            num_of_[i] += 1
        j += 1
    i += 1

max_ = [num_of_[0], 0]
for _ in range(0, SIZE):
    if num_of_[_] > max_[0]:
        max_[0] = num_of_[_]
        max_[1] = _
    _ += 1

# если есть два числа, встречающиеся больше других - будет выведено первое из них

print(array[max_[1]])
