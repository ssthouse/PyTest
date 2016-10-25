# coding=utf-8

# 使用lambda实现匿名函数

# 1.传入函数的地方传入lambda
power_2_list = map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(power_2_list))
print()


# 2.声明一个函数为lambda匿名函数
def f(x):
    return lambda: x * x


result = f(5)()
print(result)
