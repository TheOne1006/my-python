"""
匿名函数
不需要显示定义 函数
"""
# eg:
print(list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])))
# [1, 4, 9, 16, 25, 36, 49, 64, 81]

"""
lambda x: x * x 等价于
def f(x):
    return x * x
"""