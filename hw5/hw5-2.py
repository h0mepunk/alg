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


# def max_len(num1: deque,  num2: deque):
    #     if len(num1) > len(num2):
    #         return 0
    # else:
    #     num1, num2 = num2, num1
#     return len(num1)

sum_a_b = []
buf = 0
# max_len(A, B)
A = normalization_to_dec(A)
B = normalization_to_dec(B)


def sum_(num1: deque, num2: deque, buf, sum_ab):
    for i in range(len(num1), 1, -1):
        if num1:
            a = num1.pop()
            if num2:
                b = num2.pop()
                if a + b > 15:
                    sum_a_b.append(15)
                    buf = a + b - 15
                    sum_(num1, num2, buf, sum_a_b)
                else:
                    sum_a_b.append(a + b)
                    sum_(num1, num2, buf, sum_a_b)
            else:
                sum_a_b.append(a + buf)
                buf = 0
                sum_(num1, num2, buf, sum_a_b)
        else:
            if num2:
                b = num2.pop()
                sum_a_b.append(b + buf)
                buf = 0
                sum_(num1, num2, buf, sum_a_b)
            else:
                return sum_a_b


sum_(A, B, 0, sum_a_b)


print(A)
# print(normalization_to_dec(A))
# print(denormalization_to_hex(A))
print(B)
# print(normalization_to_dec(B))
# print(denormalization_to_hex(B))
print(denormalization_to_hex(sum_a_b))





