# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

a = float(input('Введите число '))
b = float(input('Введите число '))
c = float(input('Введите число '))

if a > b:
    if a > c:
        if b > c:
            print(b)
        else:
            print(c)
    else:
        print(a)
else:
    if b > c:
        if c > a:
            print(c)
        else:
            print(a)
    else:
        print(b)
