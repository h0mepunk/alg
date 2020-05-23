# Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random


SIZE_A = 4
SIZE_B = 7
MIN_ITEM = 0
MAX_ITEM = 1000
matrix = [[random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_B)] for _ in range(SIZE_A)]
print(*matrix, sep='\n')

min_el = [matrix[0][_] for _ in range(SIZE_A)]

for i in range(1, SIZE_A):
    for j in range(1, SIZE_B):
        if min_el[i] > matrix[i][j]:
            min_el[i] = matrix[i][j]
        j += 1
    i += 1

min_ = min_el[0]
for _ in range(SIZE_A):
    if min_ > min_el[_]:
        min_ = min_el[_]
    _ += _

print(min_)
