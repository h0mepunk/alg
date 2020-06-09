# Закодируйте любую строку по алгоритму Хаффмана.
from collections import deque
from binarytree import tree, bst, Node

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


class MyNode:
    def __init__(self, value, left=None, right=None, data=None):
        self.data = data
        self.value = value
        self.left = left
        self.right = right

def hffmn(s):
    h_tree = tree()
    q = deque(s)
    res = deque()
    while q:
        temp = q.popleft()
        h_tree.left = temp
        h_tree.cargo = temp[1]
        temp = q.popleft()
        h_tree.right = temp
        h_tree.cargo += temp[1]
        res.addleft(h_tree)

    return res


print(count_(str_))
print(hffmn(count_(str_)))
