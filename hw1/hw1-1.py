# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь

# https://drive.google.com/file/d/1DQw19Kq-6UF7TgHzBiKWvpor70qsKw8g/view?usp=sharing

number = int(input('Введите целое трехзначное число '))

a = number // 100
b = (number - a * 100) // 10
c = number - a * 100 - b * 10

# print(a,b,c)

sum_ = a + b + c
cmp_ = a * b * c

print('Сумма = ', sum_, 'Произведение = ', cmp_)
