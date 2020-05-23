# В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
# Это два абсолютно разных значения.
import random

SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

neg_ = []

for _ in range(0, SIZE):
    if array[_] < 0:
        neg_.append(array[_])
    _ += 1

print(neg_)

max_neg_ = neg_[0]
for _ in range(0, len(neg_)):
    if max_neg_ < neg_[_]:
        max_neg_ = neg_[_]
    _ += 1

print(max_neg_)
