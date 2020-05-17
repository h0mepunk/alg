# Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Количество элементов (n) вводится с клавиатуры.

n = int(input('Введите натуральное число '))
count = 1


def a_n(a):
    global count
    if count < n:
        a = a * -0.5
        count += 1
        return f'{a_n(a)}'
    else:
        return f'{a}'


print(a_n(1))
