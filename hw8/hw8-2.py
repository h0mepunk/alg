# Закодируйте любую строку по алгоритму Хаффмана.
from tkinter.tix import Tree

str_ = input('Введите строку: ')


def count_(s):
    set_of_letters = set()
    for i in range(0, len(s)):
        if s[i] in set_of_letters:
            i += 1
        else:
            set_of_letters.add(s[i])
            i += 1

    print(set_of_letters)
    arr = []
    counter = 0
    for i in set_of_letters:
        for j in range(0, len(s)):
            if i == s[j]:
                counter += 1
                j += 1
            else:
                j += 1
        arr.append([i, counter])
        counter = 0

    arr.sort(key=sort_arr)
    return arr


def sort_arr(a):
    return a[1]

def hffmn(s):
    h_tree = Tree()


print(count_(str_))