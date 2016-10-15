# coding=utf-8

# 取出一个list或tuple中的部分元素
src_list = ["item1", "item2", "item3", "item4", "item5"]

# result1
print("result [0:1]")
print(src_list[0:1])
print()

# result2
print("result [0:0]")
print(src_list[0:0])
print()

# result3
print("result [-1:0]")
print(src_list[-1:0])
print()

# result4
print("result [-2:-1]")
print(src_list[-2:-1])
print()

# 每隔一段 取一个item
print("result [0:len(src_list]")
print(src_list[0:len(src_list):2])
print()

