# coding=utf-8
# 一边循环一边计算的机制，称为生成器：generator

# 1.通过类似于列表的方法构造生成器, 将列表生成式的 [] 换成 ()
g = (x * x for x in [1, 2, 3, 4, 5])
print(g)
print()

# 使用generator的方法也有两种: 1.直接调用next(generator)  2.使用for循环
print("generator 使用next调用")
print(next(g))
print(next(g))
print(next(g))
print("使用for循环遍历")
for item in g:
    print(item)
print()


# 用函数实现 斐波那契 数列
def fib(max_num):
    a, b, n = 0, 1, 0
    while n < max_num:
        a, b = b, a + b
        n += 1
        print(b)


print("使用函数实现的斐波那契数列")
fib(6)
print()


# 使用generator实现的斐波那契数列
def fib(max_num):
    a, b, n = 0, 1, 0
    while n < max_num:
        a, b = b, a + b
        yield b  # 注意: yield就是每一次调用的返回值
        n += 1


print("使用generator实现的斐波那契数列")
for item in fib(6):
    print(item)
print()


# 小练习
def triangles(max_num):
    n, l = 0, [1]
    while n < max_num:
        yield l
        n += 1
        l.append(0)
        l = [l[i - 1] + l[i] for i in range(0, len(l))]


print("练习题")
for item in triangles(6):
    print(item)
