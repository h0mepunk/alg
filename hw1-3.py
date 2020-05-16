# По введенным пользователем координатам двух точек вывести уравнение прямой
# вида y = kx + b, проходящей через эти точки.

x1 = int(input('Введите x1 - координату х первой точки '))
y1 = int(input('Введите y1 - координату y первой точки '))
x2 = int(input('Введите x2 - координату х второй точки '))
y2 = int(input('Введите y2 - координату y второй точки '))

# вычислим уравнение вида (y - y1)/(y2 - y1) = (x - x1)/(x2 - x1)

k_ups = y2 - y1
k_downs = x2 - x1
k = k_ups / k_downs
b = x1 * k_ups / k_downs + y1

print('Уравнение прямой в дробном виде: у = (', k_ups, '/', k_downs, ')x +', x1 * k_ups, '/', k_downs, '+', y1)
print('Уравнение прямой в виде коэффициентов с запятой: у =', k, 'x + ', b)
