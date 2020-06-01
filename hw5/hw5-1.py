# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа)
# для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий)
# и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.

from collections import namedtuple

company = namedtuple('company', 'name, q1, q2, q3, q4, common')
companies = []


def input_company_data():
    company.name = input('Введите название компании ')
    company.q1 = input('Введите прибыль за 1 квартал ')
    company.q2 = input('Введите прибыль за 2 квартал ')
    company.q3 = input('Введите прибыль за 3 квартал ')
    company.q4 = input('Введите прибыль за 4 квартал ')
    company.common = (company.q1 + company.q2 + company.q3 + company.q4) / 4
    companies.append(company)


number_of_companies = int(input('Введите количество компаний '))

for i in range(number_of_companies):
    input_company_data()
    i += 1

max_common = [companies[0].common, 0]
for i in range(number_of_companies):
    if companies[i].common > max_common:
        max_common = [companies[i].common, i]

for i in range(number_of_companies):
    print(companies[i].name, ' Средняя годовая выручка = ', companies[i].common)

print('Компания с максимальной выручкой - ', companies[max_common[1]].name)









