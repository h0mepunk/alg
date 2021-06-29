# Определение количества различных подстрок с использованием хеш-функции.
# Пусть на вход функции дана строка. Требуется вернуть количество различных подстрок в этой строке.
# Примечание: в сумму не включаем пустую строку и строку целиком.
# Пример работы функции:
# func("papa")
# 6
# func("sova")
# 9

import hashlib

str_ = input('Введите строку: ')


def substr(s):
    set_of_substr = set()
    for i in range(0, len(s)):
        for j in range(1, len(s)):
            if hashlib.sha1(s[i: i + j].encode('utf-8')).hexdigest() in set_of_substr:
                j += 1
            else:
                set_of_substr.add(hashlib.sha1(s[i: i + j].encode('utf-8')).hexdigest())
        i += 1
    return len(set_of_substr)


print(substr(str_))


