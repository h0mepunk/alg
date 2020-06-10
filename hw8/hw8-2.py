# Закодируйте любую строку по алгоритму Хаффмана.
from collections import deque
from binarytree import tree, bst, Node

str_ = input('Введите строку: ')
result = []


class MyNode:
    def __init__(self, value, left=None, right=None, data=None):
        self.data = data
        self.value = value
        self.left = left
        self.right = right


def count_(s):
    set_of_letters = set()
    for i in range(0, len(s)):
        if s[i] in set_of_letters:
            i += 1
        else:
            set_of_letters.add(s[i])
            i += 1
    arr = []
    counter = 0
    for i in set_of_letters:
        for j in range(0, len(s)):
            if i == s[j]:
                counter += 1
                j += 1
            else:
                j += 1
        arr.append(MyNode(data=i, value=counter))
        counter = 0
    arr.sort(key=sort_arr)
    return arr


def sort_arr(a: MyNode):
    return a.value


def hffmn(s):
    while len(s) > 1:
        temp_l = s[0]
        temp_r = s[1]
        buf = MyNode(data=None, value=temp_r.value + temp_l.value)
        buf.left = temp_l
        buf.right = temp_r
        s[1] = buf
        del s[0]
        n = 0
        for i in range(1, len(s)):
            if s[n].value >= s[i].value:
                s[n], s[i] = s[i], s[n]
            n = i
            i += 1
    return s[0]


def code_table_count(tree, path):
    if tree == None:
        return result
    code_table_count(tree.left, path=path + "0")
    code_table_count(tree.right, path=path + "1")
    if tree.data != None:
        result.append([tree.data, path])

def


count_letters = count_(str_)
code_tree = hffmn(count_letters)
code_table = code_table_count(code_tree, '')
print(result)
# print(code_table_count(hffmn(count_(str_)), ''))
# print(count_(str_))
# print(hffmn(count_(str_)))
