# coding=utf-8
from functools import reduce


# 一些概念:
# 函数式编程的一个特点就是，允许把函数本身作为参数传入另一个函数，还允许返回一个函数！
# Python对函数式编程提供部分支持。由于Python允许使用变量，因此，Python不是纯函数式编程语言。

# 1.高阶函数:
# 把函数作为参数传入，这样的函数称为高阶函数，函数式编程就是指这种高度抽象的编程范式。


# map: 类似于rxJava的用法
def fun(x):
    return x * x


# 注: map返回的其实是一个Iterator print出来就是一个map object , 使用list() 其实是强制执行了所有的next方法
result = map(fun, [1, 2, 3, 4, 5])
print(list(result))
print()


# reduce
# 用法类似于map, 需要传入一个有两个参数的方法, 用于对后面每两个参数进行运算
def cat(a, b):
    return a * 10 + b


result = reduce(cat, [1, 3, 5, 7, 9])
print(result)
print()


#
# 练习1
#
# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
# 输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
def normalize(str):
    return str[0].upper() + str[0:len(str) - 1].lower()


print("practice1")
result = list(map(normalize, ['adam', 'LISA', 'barT']))
print(result)
print()


#
# 练习2
#
# Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：
def prod(l):
    return reduce(lambda x, y: x * y, l)


print("practice2")
print(prod([1, 2, 3, 4, 5]))
print()


#
# 练习3
#
# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
def str2float(string):
    i = string.find('.')
    string = string.replace('.', '')
    num = reduce(lambda x, y: x * 10 + y, map(char2num, string))
    return num / 10 ** (len(string) - i)


def char2num(c):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[c]


print("practice3")
print(str2float("123.456"))
print()
