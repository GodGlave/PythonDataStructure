#index()
#线性查找

def linear_search(li, val):
    for ind, v in enumerate(li):
        if v == val:
            return ind
    else:
        return None

li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(linear_search(li, 3))

# O(n)
# def linear_search(data_set,value):
#     for i in range(range(data_set)):
#         if data_set[i] == value:
#             return i
#     return