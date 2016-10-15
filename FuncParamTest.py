# coding=utf-8

# 必选参数(位置参数)、默认参数、可变参数、关键字参数, 命名关键字参数
# 顺序: 必选参数、默认参数、可变参数、命名关键字参数和关键字参数

# 定义包含和上面所有参数的方法


def func(a, b, c=1, *args, **kw):
    print("a:", a, "b:", b, "args:", "c:", c, args, "kw", kw)
    print()


# 各种调用方法

# result1
print("result1")
func(1, 2, 3, "arg1", "arg2", key1="value1", key2="value2")

print("result2")
func(a=1, b=2, c=3)

print("result3")
test_args = (10, 11, 12)
func(1, 2, 3, *test_args)

print("result4")
test_kw = {"key1": "value1", "key2": "value2"}
func(1, 2, 3, **test_kw)
