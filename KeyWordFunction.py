# coding=utf-8


# 1.定义关键字参数 方法
def kw_func(name, age, **kw):
    print(name)
    print(age)
    for item in kw:
        print(item, kw.get(item))
    return


# 测试调用 关键字参数  方法
# 意义在于 单个*用于表明所有的可变参数
#         两个**用于表明 除了普通的参数外, 其他的可变参数
kw_func("ssthouse", 21, **{"item1": "value1", "item2": "value2"})
print
kw_func("ssthouse", 21, item1="value1", item2="value2")


# 2.命名关键字参数
def named_kw_func(name, age, *, height, weight):
    print(height)
    print(weight)
