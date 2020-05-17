# Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

num = int(input('Введите натуральное число '))
even: int = 0
uneven: int = 0

while num // 10 != 0:
    if (num % 10) % 2 == 0:
        even += 1
        num = num // 10

    else:
        uneven += 1
        num = num // 10
if (num % 10) % 2 == 0:
    even += 1
    num = num // 10
else:
    uneven += 1
    num = num // 10

print(even, ' ', uneven)
