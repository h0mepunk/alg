# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

import random
SIZE = 10
MIN_ITEM = 2
MAX_ITEM = 99
MAX_ITEM_ = 9

array = [_ for _ in range(MIN_ITEM, MAX_ITEM + 1)]
array_ = [_ for _ in range(MIN_ITEM, MAX_ITEM_ + 1)]
res = [0] * len(array_)
print(array)
print(array_)

for i in range(0, len(array)):
    for j in range(0, len(array_)):
        if array[i] % array_[j] == 0:
            res[j] += 1
        j += 1
    i += 1

print(res)
