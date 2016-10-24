# 在一个函数中新建一个函数, 并且返回, 会引用当前函数里面的参数, 局部变量

# 所以需要记住的一点是:
# 返回闭包时牢记的一点就是：返回函数不要引用任何循环变量，或者后续会发生变化的变量。


def laze_sum(*nums):
    def sum():
        result = 0
        for i in nums:
            result += i
        return result

    return sum


sum_func = laze_sum(1, 2, 3)
print(sum_func())
print()


# 引用局部变量导致的错误
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i*i
        fs.append(f)
    return fs

count1, count2, count3 = count()
print(count1())
print(count2())
print(count3())
