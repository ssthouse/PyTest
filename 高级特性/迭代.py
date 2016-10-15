# coding=utf-8
from collections import Iterable

# 普通的迭代
src_list = ["item1", "item2", "item3", "item4", "item5"]
for item in src_list:
    print(item)
print()

# 对于dict的迭代
src_dict = {"key1": "value1", "key2": "value2", "key3": "value3"}
for key in src_dict.keys():
    print(key)
print()

for value in src_dict.values():
    print(value)
print()

for k, v in src_dict.items():
    print("key:%s value:%s" % (k, v))
print()

# 只要是可以迭代的对象, 都可以这样使用
# 那么: 哪些对象是可以迭代的呢??
# 方法是通过collections模块的Iterable类型判断：
print("判断对象是否可迭代")
print(isinstance('abc', Iterable))
print(isinstance([1, 2, 3], Iterable))
print(isinstance(123, Iterable))
print()

# 有的时候就是需要下标进行操作
# Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身：
for i, item in enumerate(["item1", "item2", "item3"]):
    print("index:%d value:%s" % (i, item))
print()

# 这里可以看到, 在循环中传入了两个变量
# 在Python里是很常见的，比如下面的代码：
for x, y in [(1, 1), (2, 2), (3, 3)]:
    print("x:%d y:%d" % (x, y))
print()
