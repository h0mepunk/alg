# Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как коллекция, элементы которой — цифры числа.
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
from collections import deque

print('Для ввода чисел 0т 10 до 15, пожалуйста, используйте ЗАГЛАВНЫЕ латинские буквы. Спасибо!')
A = deque(input('Введите первое 16-ричное число '))
B = deque(input('Введите второе 16-ричное число '))

hex_to_dec = {'1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9', 'A': '10',
              'B': '11', 'C': '12', 'D': '13', 'E': '14', 'F': '15'}
dec_to_hex = {'1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9', '10': 'A',
              '11': 'B', '12': 'C', '13': 'D', '14': 'E', '15': 'F'}


def normalization_to_dec(num):
    for i in range(0, len(num)):
        num[i] = hex((num[i]))
        i += 1
    return num


def denormalization_to_hex(num):
    for i in range(0, len(num)):
        num[i] = int(num[i])
        i += 1
    return num


print(A)
print(normalization_to_dec(A))
print(denormalization_to_hex(A))
print(B)
print(normalization_to_dec(B))
print(denormalization_to_hex(B))




