# Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
# Найдите в массиве медиану. Медианой называется элемент ряда,
# делящий его на две равные части: в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.
#
# Примечание: задачу можно решить без сортировки исходного массива.
# Но если это слишком сложно, используйте метод сортировки,
# который не рассматривался на уроках (сортировка слиянием также недопустима).

import random

SIZE = 10
MIN_ITEM = 0.0
MAX_ITEM = 49.0

array = [random.uniform(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)
