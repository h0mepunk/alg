# Определить, является ли год, который ввел пользователь, високосным или не високосным.

yr = int(input('Введите год '))

if yr // 400 == 0:
    print('високосный')
else:
    if yr // 100 == 0:
        print('не високосный')
    else:
        if yr // 4 == 0:
            print('високосный')
        else:
            print('не високосный')
