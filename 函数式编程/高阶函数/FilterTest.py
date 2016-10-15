# coding=utf-8
def is_palidrom(n):
    string = str(n)
    a, b = 0, len(string) - 1
    while a < b:
        if string[a] != string[b]:
            return False
        a += 1
        b -= 1
    return True


# 测试代码
# filter 返回的也是一个Iterator 是一个惰性序列
# 需要使用lit方法强制执行
output = filter(is_palidrom, range(1000))
print(list(output))
