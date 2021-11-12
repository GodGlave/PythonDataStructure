class BiTreeNode:
    def __init__(self, data):
        self.data = data
        self.lchild = None  # 左孩子
        self.rchild = None  # 右孩子


a = BiTreeNode("A")
b = BiTreeNode("B")
c = BiTreeNode("C")
d = BiTreeNode("D")
e = BiTreeNode("E")
f = BiTreeNode("F")
g = BiTreeNode("G")

e.lchild = a
e.rchild = g
a.rchild = c
c.lchild = b
c.rchild = d
g.rchild = f

root = e


def pro_order(root):
    """利用堆栈前序遍历"""
    if not root:
        return False
    stack = []
    node = root
    while node or stack:
        while node:  # 寻找左子树，压入栈内
            print(node.data, end=' ')
            stack.append(node)
            node = node.lchild
        node = stack.pop()
        node = node.rchild # 开始寻找右子树


def in_order(root):
    """ 利用堆栈中序遍历"""
    if not root:
        return False
    stack = []
    node = root
    while node or stack:
        while node:  # 从根结点开始，寻找左子树，把它压入栈中
            stack.append(node)
            node = node.lchild
        node = stack.pop()  # while 结束代表前一个节点没有了左子树
        print(node.data, end=' ')
        node = node.rchild  # 然后开始寻找右子树


def post_order(root):
    """利用堆栈后序遍历"""
    if not root:
        return False
    stack1 = []
    stack2 = []
    stack1.append(root)
    while stack1:  # 找出后序遍历的逆序，存放在 stack2中
        node = stack1.pop()
        if node.lchild:
            stack1.append(node.lchild)
        if node.rchild:
            stack1.append(node.rchild)
        stack2.append(node)
    while stack2:  # 将 stack2中的元素出栈，即是后序遍历序列
        print(stack2.pop().data, end=' ')

if __name__ == '__main__':
    #pro_order(root)
    #in_order(root)
    post_order(root)