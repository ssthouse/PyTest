# coding=utf-8

# 对列出的每个文件夹里面进行操作
import os

file_list = [x for x in os.listdir('.') if os.path.isfile(x)]
dir_list = [x for x in os.listdir('.') if not (os.path.isfile(x))]
print(file_list)
print(dir_list)


# 对每个文件夹里面的文件处理
def change_file_name(dir_name):
    for file in os.listdir(dir_name):
        os.rename(os.path.join(dir_item, file), os.path.join(dir_item, file) + ".gif")


for dir_item in dir_list:
    change_file_name(dir_item)
