# Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как коллекция, элементы которой — цифры числа.
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
from collections import deque

print('Для ввода чисел 0т 10 до 15, пожалуйста, используйте ЗАГЛАВНЫЕ латинские буквы. Спасибо!')
A = deque(input('Введите первое 16-ричное число '))
B = deque(input('Введите второе 16-ричное число '))

dec_to_hex = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10,
              'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
hex_to_dec = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A',
              11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
sum_a_b = []
mul_a_b = []


def normalization_to_dec(num):
    for i in range(0, len(num)):
        num[i] = dec_to_hex[num[i]]
        i += 1
    return num


def denormalization_to_hex(num):
    for i in range(0, len(num)):
        num[i] = hex_to_dec[num[i]]
        i += 1
    return num


sum_a_b = deque([])
buf = 0
A = normalization_to_dec(A)
# print(A)
B = normalization_to_dec(B)
# print(B)


def sum_(num1: deque, num2: deque, buf, sum_a_b):
        if num1:
            a = num1.pop()
            if num2:
                b = num2.pop()
                if a + b + buf > 16:
                    sum_a_b.appendleft(a + b + buf - 16)
                    buf = 1
                    sum_(num1, num2, buf, sum_a_b)
                else:
                    sum_a_b.appendleft(a + b + buf)
                    buf = 0
                    sum_(num1, num2, buf, sum_a_b)
            else:
                if a + buf > 16:
                    sum_a_b.appendleft(a + buf - 16)
                    buf = 1
                    sum_(num1, num2, buf, sum_a_b)
                else:
                    sum_a_b.appendleft(a + buf)
                    buf = 0
                    sum_(num1, num2, buf, sum_a_b)
        else:
            if num2:
                b = num2.pop()
                if b + buf > 16:
                    sum_a_b.appendleft(b + buf - 16)
                    buf = 1
                    sum_(num1, num2, buf, sum_a_b)
                else:
                    sum_a_b.appendleft(b + buf)
                    buf = 0
                    sum_(num1, num2, buf, sum_a_b)
            else:
                return sum_a_b.appendleft(buf)


sum_(A, B, 0, sum_a_b)

print(sum_a_b)
print(denormalization_to_hex(sum_a_b))





