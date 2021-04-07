"""
sorted 语法
key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序
sorted(iterable, key=None, reverse=False)
"""

arr = [5, 2, 3, 1, 4]
arr_sorted = sorted(arr)

# [1, 2, 3, 4, 5]
print(arr_sorted)
# 原数组不会变化
print(arr)

list_2 = [5, 2, 3, 1, 4]
print(list_2.sort())
print(list_2)

"""
区别二 可遍历对象
"""

print('===========')

iterable = {1: 'D', 2: 'B', 3: 'B', 4: 'E', 5: 'A'}
print(sorted(iterable))
# 根据值排序
print(sorted(iterable, key=lambda x: iterable[x]))

"""
demo
"""
array = [{"age": 20, "name": "a"}, {"age": 25, "name": "b"}, {"age": 10, "name": "c"}]
array = sorted(array, key=lambda x: x["age"])
print(array)
