# coding=utf-8
import os

# 使用range生成列表
list_one = list(range(0, 10))
print(list_one)
print()

# 生成有一定规律的list
list_two = []
for x in range(0, 10):
    list_two.append(x * x)
print(list_two)

# 使用列表生成式
list_three = [x * x for x in range(0, 10)]
print(list_three)
print()

# 列表生成式 加上判断语句
list_four = [x * x for x in range(0, 10) if (x % 2 == 0)]
print(list_four)
print()

# 使用两层循环 生成两个字符串的全排列
list_five = [m + n for m in "ABC" for n in "XYZ"]
print(list_five)
print()

# 列出当前目录的所有文件, 文件夹
dir_file_list = [d for d in os.listdir("./")]
print(dir_file_list)
print()

# 多个参数的列表生成式
d = {"key1": "value1", "key2": "value2", "key3": "value3", "key4": "value4"}
list_six = ["key:" + k + " value:" + v for k, v in d.items()]
print(list_six)
print()

# 把每个item变成小写
str_list = ["Item1", "Item2", "Item3", "Item4"]
lower_str_list = [s.lower() for s in str_list];
print(lower_str_list)
print()

# 小作业
num_str_list = ["Item1", "Item2", 3, "Item4"]
num_lower_str_list = [s.lower() for s in num_str_list if isinstance(s, str)]
print(num_lower_str_list)
print()
