from binarytree import tree, bst

a = [1, 1]

print(type(a))

a = tree(height=4, is_perfect=False)
print(a)
b = bst(height=4, is_perfect=True)
print(b)


class MyNode:
    def __init__(self, value, left=None, right=None, data=None):
        self.data = data
        self.value = value
        self.left = left
        self.right = right


c = MyNode('13')
c.left = MyNode('7')
c.right = MyNode('23')
c.left.left = MyNode('0')
c.right.left = MyNode('5')
c.left.right = MyNode('22')
print(c)