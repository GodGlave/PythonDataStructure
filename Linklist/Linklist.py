# #链表定义
class Node:
    def __init__(self, item):
        self.item = item
        self.next = None

# ##双链表定义
# class Node:
#     def __init__(self,item=None):
#         self.item=item
#         self.next=None
#         self.prior=None


#链表遍历
# a=Node(1)
# b=Node(2)
# c=Node(3)
# a.next=b
# b.next=c
#
# print(a.next.next.item)
# #
# # #列表
# # li =[1,2,3,4,5]
# # li[2]

#链表的创建头插法和尾插法
def create_linklist_head(li):
    head = Node(li[0])
    for element in li[1:]:
        node = Node(element)
        node.next = head
        head = node
    return head


def create_linklist_tail(li):
    head = Node(li[0])
    tail = head
    for element in li[1:]:
        node = Node(element)
        tail.next = node
        tail = node
    return head


def print_linklist(lk):
    while lk:
        print(lk.item, end=',')
        lk = lk.next


lk = create_linklist_tail([1, 2, 3, 6, 8])
# print(lk.item)
# print(lk.next.item)
print_linklist(lk)


# #链表节点的插入
# p.next = curNode.next
# curNode.next = p

# #链表节点的删除
# p=curNode.next
# curNode.next=curNode.next.next
# del p
#

# #双链表节点的插入
# p.next=curNode.next
# curNode.next.prior=p
# p.prior=curNode
# curNode.next=p

# #双链表节点的删除
# p=curNode.next
# curNode.next=p.next
# p.next.prior=curNode
# del p
