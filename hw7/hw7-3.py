# Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
# Найдите в массиве медиану. Медианой называется элемент ряда,
# делящий его на две равные части: в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.
#
# Примечание: задачу можно решить без сортировки исходного массива.
# Но если это слишком сложно, используйте метод сортировки,
# который не рассматривался на уроках (сортировка слиянием также недопустима).

import random

SIZE = 9
MIN_ITEM = -50.0
MAX_ITEM = 49.0

array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)


def med_search(a: array):
    flag_med_found = False
    if all(el < a[0] for el in set(a[1: SIZE])) or all(el < a[0] for el in set(a[1: SIZE])):
        flag_med_found = True
        return a[0]
    if all(el > a[0] for el in set(a[0: SIZE -1])) or all(el < a[0] for el in set(a[0: SIZE - 1])):
        flag_med_found = True
        return a[SIZE]

    for i in range(1, SIZE - 1):
        right = set(a[i + 1: SIZE])
        left = set(a[0: i - 1])
        if all(el > a[i] for el in left):
            if all(el < a[i] for el in right):
                flag_med_found = True
                return a[i]
            else:
                i += 1
        else:
            if all(el < a[i] for el in left):
                if all(el > a[i] for el in right):
                    flag_med_found = True
                    return a[i]
                else:
                    i += 1
            else:
                i += 1
    if not flag_med_found:
        return "Медиана не найдена"


print(med_search(array))

