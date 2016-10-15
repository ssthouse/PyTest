# coding=utf-8
import math

# 测试系统自定义方法
test_str = hex(16)
print(test_str)
print


# 请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：
# ax2 + bx + c = 0
def quadratic(a, b, c):
    tempDivider = math.sqrt(b * b - 4 * a * c)
    result1 = (-b + tempDivider) / 2 / a
    result2 = (-b - tempDivider) / 2 / a
    return result1, result2


# 4x*x + 4*x + 1 = 0
print()
quadratic(4, 4, 1)
print()


# 定义可变参数
def get_sum(*nums):
    sum = 0
    for num in nums:
        sum += num
    return sum


# 测试可变参数方法 get_sum
result = get_sum(1, 2, 3)
print(result)

# 测试传入list | tuple
test_list = [1, 2, 3, 4]
result = get_sum(*test_list)
print(result)
