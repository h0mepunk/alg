# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа)
# для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий)
# и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.

from collections import namedtuple

company = namedtuple('company', 'name, q1, q2, q3, q4, common')
companies = []


def input_company_data():
    name = input('Введите название компании ')
    q1 = int(input('Введите прибыль за 1 квартал '))
    q2 = int(input('Введите прибыль за 2 квартал '))
    q3 = int(input('Введите прибыль за 3 квартал '))
    q4 = int(input('Введите прибыль за 4 квартал '))
    common = (q1 + q2 + q3 + q4) / 4
    return company(name, q1, q2, q3, q4, common)


number_of_companies = int(input('Введите количество компаний '))

for i in range(0, number_of_companies):
    companies.append(input_company_data())
    i += 1

max_common = [companies[0].common, 0]
for i in range(0, number_of_companies):
    if companies[i].common > max_common[0]:
        max_common = [companies[i].common, i]
    i += 1

for i in range(0, number_of_companies):
    print(companies[i].name, ' Средняя годовая выручка = ', companies[i].common)
    i += 1

print('Компания с максимальной выручкой - ', companies[max_common[1]].name)









