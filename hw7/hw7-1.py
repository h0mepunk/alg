# Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
# Примечания:
# ● алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
# ● постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.
# Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.
import random
from collections import deque

SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 99

array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)


def b_sort(a: array):
    for i in range(0, SIZE - 1):
        fl = 0
        for j in range(0, SIZE - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                fl = 1
                j += 1
        i += 1
        if fl == 0:
            return a
    return a


def mod_sort(a: array):
    b = deque(a)
    b1 = deque()
    for i in range(0, SIZE - 1):
        if b[i] > a[i+1]:
            max = i+1
            a[i], a[i + 1] = a[i + 1], a[i]
            i += 1
        a[SIZE], a[max[1]] = a[max[1]], a[SIZE]



# print(b_sort(array))
print(mod_sort(array))
