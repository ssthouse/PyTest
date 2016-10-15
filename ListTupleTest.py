# -*- coding: utf-8 -*-
# list tuple test


# list 是可变的列表  可以追加数据
test_list = ["item1", "item2", "item3"]
print("curLength: ", len(test_list), "\n")
print(test_list)
print("\n")

# append: 在尾端添加数据
test_list.append("item4")
print("curLength: ", len(test_list), "\n")
print(test_list)
print("\n")

# tuple: 数据不可变得list, 类似于枚举, 对代码安全有利
test_tuple = ("item1", "item2", "item3")
print(test_tuple)
print("\n")
