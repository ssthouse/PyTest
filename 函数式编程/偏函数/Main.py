# coding=utf-8

# 偏函数的作用:
# 当函数的参数个数太多，需要简化时，使用functools.partial可以创建一个新的函数，这个新函数可以固定住原函数的部分参数，从而在调用时更简单。

import functools

int2 = functools.partial(int, base=2)
print(int2('10'))
print()

# max函数的偏函数
max10 = functools.partial(max, 10)
print(max10(1, 2, 3))
print(max(1, 2, 3, 11))
